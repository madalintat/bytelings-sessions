"""Day 3 tests — domain model + storage round-trip.

Loads via importlib so we don't require the package to be installed
into the swe-skills env.
"""
import importlib.util
import sys
from datetime import date
from pathlib import Path

import pytest

_HERE = Path(__file__).parent.parent
_PKG = _HERE / "src" / "habit"


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, _PKG / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# core needs to register first so storage's relative import resolves.
# But storage uses `from .core import ...`, which won't work via spec
# loading. So storage's tests load the file directly with absolute imports.
core = _load("_d130_core", "core.py")


def test_mark_done_idempotent():
    h = core.Habit(name="meditate", created=date(2026, 5, 1))
    assert h.mark_done(date(2026, 5, 8)) is True
    assert h.mark_done(date(2026, 5, 8)) is False
    assert h.log == [date(2026, 5, 8)]


def test_mark_done_keeps_log_sorted():
    h = core.Habit(name="meditate", created=date(2026, 5, 1))
    h.mark_done(date(2026, 5, 9))
    h.mark_done(date(2026, 5, 8))
    h.mark_done(date(2026, 5, 10))
    assert h.log == [date(2026, 5, 8), date(2026, 5, 9), date(2026, 5, 10)]


def test_streak_zero_when_today_missing():
    h = core.Habit(name="x", created=date(2026, 5, 1),
                   log=[date(2026, 5, 7)])
    assert h.streak(date(2026, 5, 9)) == 0


def test_streak_one():
    h = core.Habit(name="x", created=date(2026, 5, 1),
                   log=[date(2026, 5, 9)])
    assert h.streak(date(2026, 5, 9)) == 1


def test_streak_consecutive():
    log = [date(2026, 5, 7), date(2026, 5, 8), date(2026, 5, 9)]
    h = core.Habit(name="x", created=date(2026, 5, 1), log=log)
    assert h.streak(date(2026, 5, 9)) == 3


def test_streak_breaks_on_gap():
    log = [date(2026, 5, 6), date(2026, 5, 8), date(2026, 5, 9)]
    h = core.Habit(name="x", created=date(2026, 5, 1), log=log)
    assert h.streak(date(2026, 5, 9)) == 2  # 8 + 9, broken by missing 7


def test_round_trip_dict():
    h = core.Habit(name="read", created=date(2026, 5, 1),
                   log=[date(2026, 5, 8), date(2026, 5, 9)])
    d = core.to_dict(h)
    h2 = core.from_dict("read", d)
    assert h2 == h
