"""Scratchpad for poking at your data shape.

Not under test. Just a place to play with what habit data looks like
before you commit to a structure tomorrow.

Run with:  uv run python notes.py
Or open a REPL:  uv run python -i notes.py
"""
from __future__ import annotations
from datetime import date


# Sketch your data shape here. You'll replace this on Day 2 with a
# real dataclass.
example = {
    "habits": {
        "meditate": {
            "created": "2026-05-08",
            "log": ["2026-05-08", "2026-05-09"],
        },
        "read": {
            "created": "2026-05-08",
            "log": ["2026-05-09"],
        },
    }
}


def streak(log: list[str], today: date) -> int:
    """Count consecutive days back from `today` that appear in `log`.

    Naive version. Tomorrow you'll formalize this.
    """
    days = set(log)
    count = 0
    cur = today
    while cur.isoformat() in days:
        count += 1
        cur = date.fromordinal(cur.toordinal() - 1)
    return count


if __name__ == "__main__":
    today = date(2026, 5, 9)
    for name, data in example["habits"].items():
        print(f"{name}: streak {streak(data['log'], today)}")
