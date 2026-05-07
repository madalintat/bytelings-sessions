"""Tests for progress.py — load/save/advance logic."""
from datetime import date, timedelta
from pathlib import Path

from bytelings import progress as prog


def test_load_returns_default_when_file_missing(tmp_progress_path: Path):
    p = prog.load(tmp_progress_path)
    assert p.version == 1
    assert p.current_rung == 1
    assert p.completed_days == []
    assert p.streak_days == 0
    assert p.started_at  # auto-set


def test_save_then_load_roundtrip(tmp_progress_path: Path):
    p = prog.Progress(
        version=1,
        started_at="2026-05-08T10:00:00+00:00",
        current_day="day-001-uv-setup-and-pytest",
        current_rung=2,
        completed_days=[],
        completed_rungs_today=[1],
        streak_days=0,
        longest_streak=0,
        last_active_date="2026-05-08",
        notes_path="progress/notes/",
    )
    prog.save(p, tmp_progress_path)
    loaded = prog.load(tmp_progress_path)
    assert loaded == p


def test_save_is_atomic(tmp_progress_path: Path):
    """save() must not leave a partial file — uses tmp+rename."""
    p = prog.Progress(current_day="day-001")
    prog.save(p, tmp_progress_path)
    assert tmp_progress_path.exists()
    assert not tmp_progress_path.with_suffix(".json.tmp").exists()


def test_mark_rung_complete_advances_rung():
    p = prog.Progress(current_rung=2, completed_rungs_today=[1])
    p2 = prog.mark_rung_complete(p, 2)
    assert 2 in p2.completed_rungs_today
    assert p2.current_rung == 3


def test_mark_rung_complete_idempotent():
    p = prog.Progress(current_rung=3, completed_rungs_today=[1, 2])
    p2 = prog.mark_rung_complete(p, 2)
    assert p2.completed_rungs_today.count(2) == 1


def test_mark_day_complete_resets_rung_state():
    p = prog.Progress(
        current_day="day-001-uv-setup-and-pytest",
        current_rung=5,
        completed_rungs_today=[1, 2, 3, 4, 5],
    )
    p2 = prog.mark_day_complete(p, "day-001-uv-setup-and-pytest")
    assert "day-001-uv-setup-and-pytest" in p2.completed_days
    assert p2.completed_rungs_today == []
    assert p2.current_rung == 1


def test_streak_increments_on_consecutive_days():
    today = date(2026, 5, 8)
    yest = today - timedelta(days=1)
    p = prog.Progress(
        last_active_date=yest.isoformat(),
        streak_days=3,
        longest_streak=3,
    )
    p2 = prog.mark_day_complete(p, "day-002", today=today)
    assert p2.streak_days == 4
    assert p2.longest_streak == 4
    assert p2.last_active_date == today.isoformat()


def test_streak_resets_on_gap():
    today = date(2026, 5, 8)
    long_ago = today - timedelta(days=5)
    p = prog.Progress(
        last_active_date=long_ago.isoformat(),
        streak_days=10,
        longest_streak=10,
    )
    p2 = prog.mark_day_complete(p, "day-002", today=today)
    assert p2.streak_days == 1
    assert p2.longest_streak == 10  # preserved
