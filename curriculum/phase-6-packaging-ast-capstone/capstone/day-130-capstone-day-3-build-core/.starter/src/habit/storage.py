"""Storage: load/save a JSON file atomically."""
from __future__ import annotations
import json
import os
import tempfile
from datetime import date
from pathlib import Path

from .core import Habit, from_dict, to_dict


def default_data_path() -> Path:
    """Default location for the data file. Override with HABIT_DATA env var."""
    env = os.environ.get("HABIT_DATA")
    if env:
        return Path(env)
    return Path.home() / ".config" / "habit" / "data.json"


def load(path: Path) -> dict[str, Habit]:
    """Load habits from `path`. Empty dict if the file doesn't exist yet."""
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}
    data = json.loads(raw)
    habits_raw = data.get("habits", {})
    return {name: from_dict(name, h) for name, h in habits_raw.items()}


def save(path: Path, habits: dict[str, Habit]) -> None:
    """Atomically write `habits` to `path`."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"habits": {name: to_dict(h) for name, h in habits.items()}}
    # TODO (optional): turn this into a context manager so callers can
    # write `with atomic_write(path) as f: ...`. For now, the function
    # form is fine.
    tmp = tempfile.NamedTemporaryFile(
        "w", dir=path.parent, delete=False, encoding="utf-8"
    )
    try:
        json.dump(payload, tmp, indent=2, sort_keys=True)
        tmp.flush()
        os.fsync(tmp.fileno())
        tmp.close()
        os.replace(tmp.name, path)
    except Exception:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass
        raise


def mark_done(habits: dict[str, Habit], name: str, today: date) -> Habit:
    """Mark `name` done today, auto-creating the habit if missing.

    Returns the updated Habit.
    """
    if name not in habits:
        habits[name] = Habit(name=name, created=today)
    habits[name].mark_done(today)
    return habits[name]
