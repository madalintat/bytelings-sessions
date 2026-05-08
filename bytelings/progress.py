"""Load, save, and update progress state for the swe runner."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

DEFAULT_PROGRESS_PATH = Path("progress/progress.json")
TOTAL_RUNGS = 5


@dataclass
class Progress:
    version: int = 2
    started_at: str = ""
    current_day: str = ""
    current_rung: int = 1
    completed_days: list[str] = field(default_factory=list)
    completed_rungs_today: list[int] = field(default_factory=list)
    streak_days: int = 0
    longest_streak: int = 0
    last_active_date: str = ""
    notes_path: str = "progress/notes/"
    patterns_seen: list[str] = field(default_factory=list)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _today_iso() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def load(path: Path = DEFAULT_PROGRESS_PATH) -> Progress:
    """Return Progress from disk, or a fresh default if the file is missing.

    Auto-migrates v1 schemas to v2 in place: any older progress.json
    that predates the patterns_seen field gets migrated and saved back.
    Slug back-compat for the curriculum tree itself lives in locator.py.
    """
    if not path.exists():
        # last_active_date stays empty until the first day actually completes.
        # Otherwise mark_day_complete sees today == today and skips the streak
        # bump, leaving the very first completion at 0.
        return Progress(started_at=_now_iso(), last_active_date="")
    data = json.loads(path.read_text())
    migrated = False
    if data.get("version", 1) == 1:
        data.setdefault("patterns_seen", [])
        data["version"] = 2
        migrated = True
    p = Progress(**data)
    if migrated:
        save(p, path)
    return p


def save(p: Progress, path: Path = DEFAULT_PROGRESS_PATH) -> None:
    """Atomically write progress to disk via tmp-file + rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(asdict(p), indent=2))
    tmp.replace(path)


def mark_rung_complete(p: Progress, rung: int) -> Progress:
    """Record a rung as done and advance current_rung if applicable."""
    already_recorded = rung in p.completed_rungs_today
    already_past = rung < p.current_rung
    if already_recorded and already_past:
        return p
    if not already_recorded:
        p.completed_rungs_today = sorted({*p.completed_rungs_today, rung})
    if rung >= p.current_rung and p.current_rung < TOTAL_RUNGS:
        p.current_rung = rung + 1
    return p


def mark_day_complete(
    p: Progress,
    day_slug: str,
    today: date | None = None,
) -> Progress:
    """Mark a whole day complete; reset rung state; update streak."""
    today = today or datetime.now(timezone.utc).date()
    today_s = today.isoformat()

    if day_slug not in p.completed_days:
        p.completed_days.append(day_slug)
    p.completed_rungs_today = []
    p.current_rung = 1

    yesterday_s = (today - timedelta(days=1)).isoformat()
    if p.last_active_date != today_s:
        p.streak_days = p.streak_days + 1 if p.last_active_date == yesterday_s else 1
    p.longest_streak = max(p.longest_streak, p.streak_days)
    p.last_active_date = today_s
    return p


def advance_after_pass(
    p: Progress,
    day_slug: str,
    rung: int,
    next_day_slug: str | None,
) -> Progress:
    """Compose mark_rung + (if rung==5) mark_day + jump to next day's rung 1.

    Single source for the "post-pass" state transition shared by
    `swe done` and the watcher.
    """
    p = mark_rung_complete(p, rung)
    if rung == TOTAL_RUNGS:
        p = mark_day_complete(p, day_slug)
        if next_day_slug is not None:
            p.current_day = next_day_slug
            p.current_rung = 1
    return p
