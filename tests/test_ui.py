"""Smoke tests for the persistent watcher TUI (RunnerUI).

These don't open a real Live (no terminal), they just verify that the
state-transition methods mutate the layout cell in place — i.e. each
call replaces the body renderable instead of appending a new one. That's
the bug that was causing rustlings-style behavior to fail.
"""
from __future__ import annotations

from rich.panel import Panel

from bytelings import ui
from bytelings.locator import Rung


def _fake_rungs(day_dir):
    return [
        Rung(1, day_dir / "concept.md", None, "Read the concept"),
        Rung(2, day_dir / "02_fluency.py",
             day_dir / "02_fluency_test.py", "Fluency drill"),
        Rung(3, day_dir / "03_guided.py",
             day_dir / "03_guided_test.py", "Guided implement"),
        Rung(4, day_dir / "04_solo.py",
             day_dir / "04_solo_test.py", "Solo implement"),
        Rung(5, day_dir / "05_apply.py", None, "Apply"),
    ]


def test_runner_ui_starts_idle(tmp_path):
    runner = ui.RunnerUI()
    assert runner.run_count == 0
    assert isinstance(runner.body_renderable, Panel)


def test_runner_ui_set_running_increments_and_replaces_body(tmp_path):
    runner = ui.RunnerUI()
    idle_body = runner.body_renderable
    runner.set_running()
    assert runner.run_count == 1
    assert runner.body_renderable is not idle_body
    assert runner.body_renderable.border_style == "yellow"


def test_runner_ui_consecutive_state_changes_replace_in_place(tmp_path):
    runner = ui.RunnerUI()
    runner.set_running()
    after_running = runner.body_renderable

    runner.set_fail("AssertionError: nope")
    after_fail = runner.body_renderable

    runner.set_running()
    after_running_2 = runner.body_renderable

    runner.set_pass("Rung 2: Fluency drill")
    after_pass = runner.body_renderable

    # Each transition replaces the cell, never stacks.
    assert after_running is not after_fail
    assert after_fail is not after_running_2
    assert after_running_2 is not after_pass
    assert after_fail.border_style == "red"
    assert after_pass.border_style == "green"


def test_runner_ui_run_count_only_advances_on_set_running():
    runner = ui.RunnerUI()
    runner.set_running()
    runner.set_fail("oops")
    runner.set_pass("Rung X")
    runner.set_message("hi")
    # set_running was called once; everything else preserves the count.
    assert runner.run_count == 1
    runner.set_running()
    assert runner.run_count == 2


def test_runner_ui_set_rungs_updates_layout(tmp_path):
    runner = ui.RunnerUI()
    rungs = _fake_rungs(tmp_path)
    runner.set_rungs(rungs, current=2, completed=[1])
    # The rungs cell should now hold a Table, not the placeholder.
    rendered = runner._layout["rungs"].renderable
    assert rendered.__class__.__name__ == "Table"


def test_runner_ui_paused_is_a_noop_when_not_started():
    runner = ui.RunnerUI()
    # Should not raise even though Live was never started.
    with runner.paused():
        pass
    assert runner.run_count == 0
