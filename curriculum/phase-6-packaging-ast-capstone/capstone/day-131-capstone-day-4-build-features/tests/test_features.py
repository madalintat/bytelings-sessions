"""Day 4 tests — feature additions in core.py."""
import importlib.util
import sys
from datetime import date
from pathlib import Path

_HERE = Path(__file__).parent.parent
_PKG = _HERE / "src" / "habit"


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, _PKG / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


core = _load("_d131_core", "core.py")


def test_filter_log_basic():
    h = core.Habit("x", date(2026, 1, 1),
                   log=[date(2026, 5, 1), date(2026, 5, 5), date(2026, 5, 8)])
    out = core.filter_log(h, date(2026, 5, 5))
    assert out == [date(2026, 5, 5), date(2026, 5, 8)]


def test_filter_log_empty():
    h = core.Habit("x", date(2026, 1, 1), log=[])
    assert core.filter_log(h, date(2026, 5, 1)) == []


def test_filter_log_all_excluded():
    h = core.Habit("x", date(2026, 1, 1), log=[date(2026, 1, 1)])
    assert core.filter_log(h, date(2026, 5, 1)) == []


def test_clear_wipes_log():
    h = core.Habit("x", date(2026, 1, 1),
                   log=[date(2026, 5, 1), date(2026, 5, 8)])
    h.clear()
    assert h.log == []


def test_sort_key_streak_orders_longest_first():
    today = date(2026, 5, 9)
    a = core.Habit("a", date(2026, 5, 1),
                   log=[date(2026, 5, 9)])  # streak 1
    b = core.Habit("b", date(2026, 5, 1),
                   log=[date(2026, 5, 7), date(2026, 5, 8), date(2026, 5, 9)])  # streak 3
    c = core.Habit("c", date(2026, 5, 1),
                   log=[date(2026, 5, 9), date(2026, 5, 8)])  # streak 2
    ordered = sorted([a, b, c], key=core.sort_key_streak(today))
    assert [h.name for h in ordered] == ["b", "c", "a"]


def test_sort_key_streak_ties_break_by_name():
    today = date(2026, 5, 9)
    a = core.Habit("apple", date(2026, 5, 1), log=[date(2026, 5, 9)])
    b = core.Habit("banana", date(2026, 5, 1), log=[date(2026, 5, 9)])
    ordered = sorted([b, a], key=core.sort_key_streak(today))
    assert [h.name for h in ordered] == ["apple", "banana"]
