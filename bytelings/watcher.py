"""File-watching + pytest-running heart of the swe runner."""
from __future__ import annotations

import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from . import locator, progress as progress_mod, ui

DEBOUNCE_SECONDS = 0.4


@dataclass
class TestResult:
    passed: bool
    summary: str
    raw: str


def run_pytest(test_file: Path) -> TestResult:
    """Run pytest against a single test file; return parsed result."""
    if not test_file.exists():
        return TestResult(False, f"Test file not found: {test_file}", "")
    # Skip `uv run`: we're already in the venv (sys.executable proves it).
    # Saves ~150-400ms of uv resolve overhead per save event.
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file),
         "-x", "--tb=short", "-q"],
        capture_output=True,
        text=True,
    )
    raw = (proc.stdout or "") + (proc.stderr or "")
    if proc.returncode == 0:
        return TestResult(True, "All tests passed.", raw)
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

    def on_modified(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        path_str = str(event.src_path)
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

    # Auto-advance past rung 1 (concept.md is silent reading).
    if p.current_rung == 1:
        p = progress_mod.mark_rung_complete(p, 1)
        progress_mod.save(p, progress_path)
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
                "(no automated tests — run `uv run swe done` to advance)",
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
            rung = rungs[0]
            ui.header(f"Next up: {day.slug}")
            ui.rung_table(rungs, p.current_rung, [])
        else:
            p = progress_mod.mark_rung_complete(p, rung.number)
            progress_mod.save(p, progress_path)
            rung = locator.rung_for(p, rungs)
            ui.header(f"{day.slug} — Rung {rung.number}: {rung.name}")

    handler = _RungHandler(on_change=on_save)
    observer = Observer()
    observer.schedule(handler, str(day.path), recursive=False)
    observer.start()
    try:
        if rung.test_file is not None:
            on_save(str(rung.file))
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        ui.header("Stopping watcher. See you tomorrow.")
    finally:
        observer.stop()
        observer.join()
