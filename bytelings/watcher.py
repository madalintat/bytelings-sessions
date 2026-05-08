"""File-watching + pytest-running heart of the bytelings runner.

The watcher owns three things:

1. A ``watchdog`` observer scoped to the current day's directory.
2. A persistent ``RunnerUI`` (alt-screen Live + Layout) that shows the
   day, rung table, latest test status, and key legend, all in place.
3. A keystroke loop on stdin (``r`` rerun, ``h`` hint, ``l`` list, ``c``
   change day, ``q`` quit).

Saves and keystrokes both mutate the same ``RunnerUI`` — that's why
``RunnerUI`` is internally locked.
"""
from __future__ import annotations

import contextlib
import os
import select
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from . import locator, progress as progress_mod, ui

DEBOUNCE_SECONDS = 0.4
DEBUG = bool(os.environ.get("BYTELINGS_DEBUG"))


@dataclass
class TestResult:
    passed: bool
    summary: str
    raw: str


def _project_python_path() -> Path | None:
    """Return the student project's venv Python if it exists, else None."""
    for candidate in (Path(".venv/bin/python"), Path(".venv/Scripts/python.exe")):
        if candidate.exists():
            return candidate
    return None


def _project_python() -> str:
    """Pick the Python that has pytest installed.

    `bytelings` is typically installed via `uv tool install`, so its own
    `sys.executable` lives in an isolated tool venv with no pytest. The
    student runs `uv sync` inside their working folder, which creates
    `.venv/` next to `pyproject.toml` with pytest. Prefer that one.
    """
    p = _project_python_path()
    return str(p) if p else sys.executable


def uv_sync_done() -> bool:
    """True iff the student's `.venv` exists and has pytest importable."""
    py = _project_python_path()
    if py is None:
        return False
    proc = subprocess.run(
        [str(py), "-c", "import pytest"],
        capture_output=True, text=True,
    )
    return proc.returncode == 0


def run_pytest(test_file: Path) -> TestResult:
    """Run pytest against a single test file; return parsed result."""
    if not test_file.exists():
        return TestResult(False, f"Test file not found: {test_file}", "")
    proc = subprocess.run(
        [_project_python(), "-m", "pytest", str(test_file),
         "-x", "--tb=short", "-q"],
        capture_output=True,
        text=True,
    )
    raw = (proc.stdout or "") + (proc.stderr or "")
    if proc.returncode == 0:
        return TestResult(True, "All tests passed.", raw)
    if "No module named pytest" in raw:
        return TestResult(
            False,
            "pytest isn't installed in this folder's .venv yet.\n"
            "Run `uv sync` here, then save the file again.",
            raw,
        )
    return TestResult(False, truncate_to_first_failure(raw), raw)


def truncate_to_first_failure(raw: str) -> str:
    """Keep just enough output to show the first failure."""
    lines = raw.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("FAILED "):
            return "\n".join(lines[: i + 1])
    return "\n".join(lines[:30])


class _RungHandler(FileSystemEventHandler):
    """File-event handler bound to a single (day, rung) pair."""

    def __init__(self, on_change):
        self._on_change = on_change
        self._last_run = 0.0

    def _maybe_fire(self, path_str: str) -> None:
        if not path_str.endswith(".py"):
            return
        # Editors and pytest itself touch __pycache__; ignore.
        if "__pycache__" in path_str:
            return
        now = time.time()
        if now - self._last_run < DEBOUNCE_SECONDS:
            return
        self._last_run = now
        if DEBUG:
            sys.stderr.write(f"[bytelings:debug] save event → {path_str}\n")
        self._on_change(path_str)

    def on_modified(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        self._maybe_fire(str(event.src_path))

    def on_created(self, event: FileSystemEvent) -> None:
        # Atomic-save editors (vim with writebackup, some IDEs) write a
        # temp file and rename it over the original — that lands as a
        # create/move, not a modify.
        if event.is_directory:
            return
        self._maybe_fire(str(event.src_path))

    def on_moved(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        dest = getattr(event, "dest_path", "") or ""
        self._maybe_fire(str(dest))


@contextlib.contextmanager
def _cbreak_stdin():
    """Put stdin into character-at-a-time mode for the duration of the block.

    No-op when stdin isn't a TTY (background process, piped input, CI).
    Restores the previous tty state on exit, even on exception.
    """
    if not sys.stdin.isatty():
        yield False
        return
    import termios, tty  # POSIX only — we're not aiming at Windows yet
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        yield True
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _read_key() -> str | None:
    """Return one queued keystroke, or None if none is available right now."""
    if not sys.stdin.isatty():
        return None
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None


def _wait_for_uv_sync(is_day_one: bool) -> bool:
    """Block until `.venv` exists with pytest. Return False on Ctrl-C."""
    if uv_sync_done():
        return True
    if is_day_one:
        hint = (
            "[bold yellow]Rung 1 — run `uv sync` first[/bold yellow]\n\n"
            "That's the whole point of Day 1. In another terminal:\n\n"
            "    [cyan]uv sync[/cyan]\n\n"
            "I'll watch for the .venv to appear, then auto-advance."
        )
    else:
        hint = (
            "[bold yellow]Need to run `uv sync` first[/bold yellow]\n\n"
            "Your local `.venv` is missing or pytest isn't installed there.\n"
            "In another terminal:\n\n"
            "    [cyan]uv sync[/cyan]\n\n"
            "I'll pick it up automatically once it's done."
        )
    ui.console.print(hint)
    last_hint = time.time()
    try:
        while not uv_sync_done():
            time.sleep(1.0)
            if time.time() - last_hint > 30:
                ui.console.print("[dim]…still waiting for `uv sync`…[/dim]")
                last_hint = time.time()
    except KeyboardInterrupt:
        ui.header("Stopping watcher. Run `uv sync`, then `bytelings` again.")
        return False
    return True


def _show_concept_blocking(day) -> None:
    """Print a day's README.md to the regular terminal and wait for a key."""
    concept = day.path / "README.md"
    ui.header(f"Concept: {day.slug}")
    if concept.is_file():
        ui.console.print(concept.read_text())
    else:
        ui.console.print(f"[dim]No README.md for {day.slug}[/dim]")
    ui.console.print("\n[dim](press any key to return)[/dim]")
    _wait_any_key()


def _show_list_blocking(p, current_day_slug: str) -> None:
    """Print every day with completion markers; wait for a key."""
    completed = set(p.completed_days)
    for d in locator.all_days():
        if d.slug == current_day_slug:
            marker = "[cyan]→[/cyan]"
        elif d.slug in completed:
            marker = "[green]✔[/green]"
        else:
            marker = "[dim]○[/dim]"
        ui.console.print(f"{marker} {d.slug} [dim]({d.module})[/dim]")
    ui.console.print("\n[dim](press any key to return)[/dim]")
    _wait_any_key()


def _wait_any_key() -> None:
    """Block until the user presses any key. cbreak-aware."""
    if not sys.stdin.isatty():
        return
    # If we're already in cbreak (the watcher's main loop), a single
    # read is enough. If we're in cooked mode (after stop()), readline.
    try:
        sys.stdin.read(1)
    except (KeyboardInterrupt, EOFError):
        pass


def _prompt_for_day(days) -> str | None:
    """Prompt for a day slug or number on the cooked terminal. Returns slug."""
    ui.console.print(
        "[bold]Change day[/bold] — enter day number (e.g. 7) or slug, "
        "or press Enter to cancel:"
    )
    try:
        answer = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        return None
    if not answer:
        return None
    if answer.isdigit():
        n = int(answer)
        target = next((d for d in days if d.number == n), None)
    else:
        target = next((d for d in days if d.slug == answer), None)
    if target is None:
        ui.console.print(f"[red]No such day: {answer}[/red]")
        ui.console.print("[dim](press any key to return)[/dim]")
        _wait_any_key()
        return None
    return target.slug


def watch(progress_path: Path = progress_mod.DEFAULT_PROGRESS_PATH) -> None:
    """Watch the current rung's files and run tests on save until exit."""
    p = progress_mod.load(progress_path)
    day = locator.current_or_next_day(p)
    if day is None:
        ui.header("All 135 days complete!")
        return

    if p.current_day != day.slug:
        p.current_day = day.slug
        p.current_rung = 1
        p.completed_rungs_today = []
        progress_mod.save(p, progress_path)

    rungs = locator.rungs_of(day)

    # Rung 1 = "Read the concept". On Day 1 the concept IS `uv sync`,
    # so we gate on that. For any day, `uv sync` is a hard precondition
    # — without `.venv`, no rung can run pytest. Wait for it before
    # going any further. This happens BEFORE we start the live UI so
    # the user can read the hint in the regular terminal.
    if p.current_rung == 1:
        is_day_one = day.number == 1
        if not _wait_for_uv_sync(is_day_one):
            return  # student hit Ctrl-C while we were waiting
        p = progress_mod.mark_rung_complete(p, 1)
        progress_mod.save(p, progress_path)
        if is_day_one:
            ui.banner_pass(
                "Rung 1: uv sync",
                "(.venv is ready — the watcher will run pytest from it)",
            )
        else:
            ui.banner_pass(
                "Rung 1: Read the concept",
                "(auto-completed — open README.md whenever you want to refer back)",
            )

    rung = locator.rung_for(p, rungs)

    runner = ui.RunnerUI()
    runner.set_title(f"{day.slug} — Rung {rung.number}: {rung.name}")
    runner.set_rungs(rungs, p.current_rung, p.completed_rungs_today)

    nonlocal_state: dict = {"next_day_slug": None}

    def on_save(_path: str) -> None:
        nonlocal p, rung, rungs, day
        # Apply rungs declare apply_test.py as optional in _RUNG_SPECS;
        # many days don't ship one. Treat a declared-but-missing test
        # file the same as test_file=None — "no automated tests."
        no_tests = rung.test_file is None or not rung.test_file.exists()
        if no_tests:
            runner.set_message(
                f"[bold]Rung {rung.number}:[/bold] no automated tests.\n\n"
                "Run [cyan]bytelings done[/cyan] to advance.",
                border="cyan",
            )
            return
        runner.set_running()
        result = run_pytest(rung.test_file)
        if not result.passed:
            runner.set_fail(result.summary)
            return

        if rung.number == progress_mod.TOTAL_RUNGS:
            # Find next day before applying state change so we save once.
            next_day = next(
                (d for d in locator.all_days()
                 if d.slug not in p.completed_days and d.slug != day.slug),
                None,
            )
            p = progress_mod.advance_after_pass(
                p, day.slug, rung.number,
                next_day.slug if next_day else None,
            )
            progress_mod.save(p, progress_path)
            runner.set_day_complete(day.slug, p.streak_days)
            if next_day is None:
                runner.set_title("All 135 days complete!")
                return
            day = next_day
            rungs = locator.rungs_of(day)
            # New day's Rung 1 ("Read the concept") auto-passes so the
            # student lands on Rung 2.
            p = progress_mod.mark_rung_complete(p, 1)
            progress_mod.save(p, progress_path)
            rung = locator.rung_for(p, rungs)
            # Re-aim the observer at the new day's directory; otherwise
            # saves in the new day silently fall on the floor.
            observer.unschedule_all()
            observer.schedule(handler, str(day.path), recursive=False)
            runner.set_title(f"{day.slug} — Rung {rung.number}: {rung.name}")
            runner.set_rungs(rungs, p.current_rung, p.completed_rungs_today)
        else:
            runner.set_pass(f"Rung {rung.number}: {rung.name}")
            p = progress_mod.mark_rung_complete(p, rung.number)
            progress_mod.save(p, progress_path)
            rung = locator.rung_for(p, rungs)
            runner.set_title(f"{day.slug} — Rung {rung.number}: {rung.name}")
            runner.set_rungs(rungs, p.current_rung, p.completed_rungs_today)

    handler = _RungHandler(on_change=on_save)
    observer = Observer()
    observer.schedule(handler, str(day.path), recursive=False)
    observer.start()

    runner.start()
    try:
        # Initial run so the body shows real status, not the idle hint.
        # on_save handles the no-test-file case internally.
        on_save(str(rung.file))

        with _cbreak_stdin() as keys_active:
            while True:
                if not keys_active:
                    time.sleep(0.5)
                    continue
                key = _read_key()
                if key is None:
                    time.sleep(0.05)
                    continue
                if key == "q":
                    break
                if key == "r":
                    on_save(str(rung.file))
                elif key == "h":
                    with runner.paused():
                        _show_concept_blocking(day)
                elif key == "l":
                    with runner.paused():
                        _show_list_blocking(p, day.slug)
                elif key == "c":
                    with runner.paused():
                        slug = _prompt_for_day(locator.all_days())
                    if slug is not None:
                        nonlocal_state["next_day_slug"] = slug
                        break
    except KeyboardInterrupt:
        pass
    finally:
        runner.stop()
        observer.stop()
        observer.join()

    if nonlocal_state["next_day_slug"]:
        p.current_day = nonlocal_state["next_day_slug"]
        p.current_rung = 1
        p.completed_rungs_today = []
        progress_mod.save(p, progress_path)
        ui.header(f"Switching to {p.current_day} — restarting watcher.")
        watch(progress_path)
        return
    ui.header("Stopping watcher. See you tomorrow.")
