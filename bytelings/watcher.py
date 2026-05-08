"""File-watching + pytest-running heart of the bytelings runner."""
from __future__ import annotations

import contextlib
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

KEY_LEGEND = (
    "[dim]keys: [bold]r[/bold] rerun  "
    "[bold]h[/bold] hint  [bold]l[/bold] list  "
    "[bold]c[/bold] change day  [bold]q[/bold] quit[/dim]"
)


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
    """True iff the student's `.venv` exists and has pytest importable.

    This is Rung 1's check on Day 1 (and a precondition for every rung
    after): without `uv sync`, no test can run, so the watcher can't do
    its job.
    """
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
    """Block until `.venv` exists with pytest. Return False on Ctrl-C.

    Polls once a second and re-prints a hint every ~10s so the student
    sees something is alive while they go run `uv sync`.
    """
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

    # Rung 1 = "Read the concept". On Day 1 specifically, the concept IS
    # `uv sync`, so we check that here. For other days, `uv sync` is still
    # a hard precondition — without `.venv`, no rung can run pytest, so
    # we wait for it before going any further.
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
                "(auto-completed — open concept.md whenever you want to refer back)",
            )

    rung = locator.rung_for(p, rungs)
    ui.header(f"{day.slug} — Rung {rung.number}: {rung.name}")
    ui.rung_table(rungs, p.current_rung, p.completed_rungs_today)

    def on_save(_path: str) -> None:
        nonlocal p, rung, rungs, day
        if rung.test_file is None:
            ui.banner_pass(
                f"Rung {rung.number}",
                "(no automated tests — run `bytelings done` to advance)",
            )
            return
        result = run_pytest(rung.test_file)
        if not result.passed:
            ui.banner_fail(result.summary)
            return

        ui.banner_pass(f"Rung {rung.number}: {rung.name}")
        if rung.number == progress_mod.TOTAL_RUNGS:
            # Find next day before applying state change so we can save once.
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
            ui.banner_day_complete(day.slug, p.streak_days)
            if next_day is None:
                ui.header("All 135 days complete!")
                return
            day = next_day
            rungs = locator.rungs_of(day)
            # New day's Rung 1 is "Read the concept" (no test_file). Auto-pass it
            # like the watcher's startup path so the student lands on Rung 2.
            p = progress_mod.mark_rung_complete(p, 1)
            progress_mod.save(p, progress_path)
            rung = locator.rung_for(p, rungs)
            # Re-aim the observer at the new day's directory; otherwise saves
            # in the new day silently fall on the floor.
            observer.unschedule_all()
            observer.schedule(handler, str(day.path), recursive=False)
            ui.header(f"Next up: {day.slug} — Rung {rung.number}: {rung.name}")
            ui.rung_table(rungs, p.current_rung, p.completed_rungs_today)
        else:
            p = progress_mod.mark_rung_complete(p, rung.number)
            progress_mod.save(p, progress_path)
            rung = locator.rung_for(p, rungs)
            ui.header(f"{day.slug} — Rung {rung.number}: {rung.name}")

    handler = _RungHandler(on_change=on_save)
    observer = Observer()
    observer.schedule(handler, str(day.path), recursive=False)
    observer.start()

    def show_hint() -> None:
        concept = day.path / "concept.md"
        if concept.is_file():
            ui.header(f"Concept: {day.slug}")
            ui.console.print(concept.read_text())
        else:
            ui.console.print(f"[dim]No concept.md for {day.slug}[/dim]")

    def show_list() -> None:
        completed = set(p.completed_days)
        for d in locator.all_days():
            if d.slug == day.slug:
                marker = "[cyan]→[/cyan]"
            elif d.slug in completed:
                marker = "[green]✔[/green]"
            else:
                marker = "[dim]○[/dim]"
            ui.console.print(f"{marker} {d.slug} [dim]({d.module})[/dim]")

    def change_day() -> bool:
        """Prompt for a day; switch to it. Returns True if the watcher should restart."""
        # Drop out of cbreak so input() works normally.
        ui.console.print(
            "[bold]Change day[/bold] — enter day number (e.g. 7) or slug, "
            "or press Enter to cancel:"
        )
        try:
            answer = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            return False
        if not answer:
            return False
        days = locator.all_days()
        target = None
        if answer.isdigit():
            n = int(answer)
            target = next((d for d in days if d.number == n), None)
        else:
            target = next((d for d in days if d.slug == answer), None)
        if target is None:
            ui.console.print(f"[red]No such day: {answer}[/red]")
            return False
        nonlocal_state["next_day_slug"] = target.slug
        return True

    nonlocal_state: dict = {"next_day_slug": None, "quit": False}
    try:
        if rung.test_file is not None:
            on_save(str(rung.file))
        ui.console.print(KEY_LEGEND)
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
                    nonlocal_state["quit"] = True
                    break
                if key == "r":
                    if rung.test_file is not None:
                        on_save(str(rung.file))
                    else:
                        ui.console.print(
                            "[dim](no automated tests — run `bytelings done` to advance)[/dim]"
                        )
                    ui.console.print(KEY_LEGEND)
                elif key == "h":
                    show_hint()
                    ui.console.print(KEY_LEGEND)
                elif key == "l":
                    show_list()
                    ui.console.print(KEY_LEGEND)
                elif key == "c":
                    # input() needs canonical mode; pop out of cbreak briefly.
                    import termios, tty
                    fd = sys.stdin.fileno()
                    saved = termios.tcgetattr(fd)
                    termios.tcsetattr(fd, termios.TCSADRAIN, saved)  # leave alone
                    try:
                        # Restore canonical mode for input()
                        cooked = termios.tcgetattr(fd)
                        cooked[3] |= termios.ICANON | termios.ECHO
                        termios.tcsetattr(fd, termios.TCSADRAIN, cooked)
                        if change_day():
                            break
                    finally:
                        tty.setcbreak(fd)
                    ui.console.print(KEY_LEGEND)
    except KeyboardInterrupt:
        pass
    finally:
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
