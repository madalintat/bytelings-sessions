"""Domain model: Habit + streak logic.

A few TODOs are left for you. The shape and tests are real.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Habit:
    """One tracked habit."""

    name: str
    created: date
    log: list[date] = field(default_factory=list)

    def mark_done(self, today: date) -> bool:
        """Record `today` in the log. Idempotent.

        Returns True if a new entry was added, False if it was already there.
        """
        if today in self.log:
            return False
        self.log.append(today)
        self.log.sort()
        return True

    def streak(self, today: date) -> int:
        """Consecutive days back from `today` that appear in the log.

        Examples:
            Logged today only        -> 1
            Logged today + yesterday -> 2
            Logged today + 2 days ago (skip yesterday) -> 1
            Not logged today         -> 0
        """
        # TODO: build a set from self.log, walk backward from today,
        # increment a counter while the day is in the set.
        raise NotImplementedError


def to_dict(habit: Habit) -> dict:
    """Serialize a Habit to JSON-friendly dict (dates -> ISO strings)."""
    return {
        "created": habit.created.isoformat(),
        "log": [d.isoformat() for d in habit.log],
    }


def from_dict(name: str, data: dict) -> Habit:
    """Deserialize a Habit from JSON-friendly dict."""
    return Habit(
        name=name,
        created=date.fromisoformat(data["created"]),
        log=[date.fromisoformat(s) for s in data.get("log", [])],
    )
