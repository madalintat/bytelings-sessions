"""Domain model — extended for day 4 features."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Habit:
    name: str
    created: date
    log: list[date] = field(default_factory=list)

    def mark_done(self, today: date) -> bool:
        if today in self.log:
            return False
        self.log.append(today)
        self.log.sort()
        return True

    def streak(self, today: date) -> int:
        days = set(self.log)
        count = 0
        cur = today
        while cur in days:
            count += 1
            cur -= timedelta(days=1)
        return count

    def clear(self) -> None:
        """Wipe the log. Used by `habit reset`."""
        self.log.clear()


def filter_log(habit: Habit, since: date) -> list[date]:
    """Return entries from `habit.log` on or after `since`, sorted ascending.

    >>> from datetime import date
    >>> h = Habit("x", date(2026, 1, 1), log=[date(2026, 5, 1), date(2026, 5, 8)])
    >>> filter_log(h, date(2026, 5, 5))
    [datetime.date(2026, 5, 8)]
    """
    return sorted(d for d in habit.log if d >= since)


def sort_key_streak(today: date):
    """Key function for `sorted(...)`. Sorts longest streak first, then by name."""
    def key(habit: Habit) -> tuple[int, str]:
        return (-habit.streak(today), habit.name)
    return key


def to_dict(habit: Habit) -> dict:
    return {
        "created": habit.created.isoformat(),
        "log": [d.isoformat() for d in habit.log],
    }


def from_dict(name: str, data: dict) -> Habit:
    return Habit(
        name=name,
        created=date.fromisoformat(data["created"]),
        log=[date.fromisoformat(s) for s in data.get("log", [])],
    )
