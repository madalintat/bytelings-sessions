"""Parametrized streak edge cases."""
from datetime import date

import pytest


@pytest.mark.parametrize(
    "log,today,expected",
    [
        ([], date(2026, 5, 9), 0),
        ([date(2026, 5, 9)], date(2026, 5, 9), 1),
        ([date(2026, 5, 8), date(2026, 5, 9)], date(2026, 5, 9), 2),
        # gap breaks the streak
        ([date(2026, 5, 6), date(2026, 5, 8), date(2026, 5, 9)],
         date(2026, 5, 9), 2),
        # all in the future relative to today
        ([date(2026, 6, 1)], date(2026, 5, 9), 0),
        # today missing
        ([date(2026, 5, 8)], date(2026, 5, 9), 0),
    ],
    ids=["empty", "today-only", "two-day", "gap", "all-future", "today-missing"],
)
def test_streak_table(core_mod, log, today, expected):
    h = core_mod.Habit("x", date(2026, 1, 1), log=list(log))
    assert h.streak(today) == expected
