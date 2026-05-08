"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def E(user, priority, time):
    return {"user": user, "priority": priority, "time": time}


def test_priority_first():
    events = [E("a", 2, 1), E("b", 1, 2)]
    assert ex.sort_events(events) == [E("b", 1, 2), E("a", 2, 1)]


def test_time_breaks_priority_tie():
    events = [E("a", 1, 10), E("b", 1, 5)]
    assert ex.sort_events(events) == [E("b", 1, 5), E("a", 1, 10)]


def test_user_breaks_all_ties():
    events = [E("c", 1, 5), E("a", 1, 5), E("b", 1, 5)]
    assert ex.sort_events(events) == [E("a", 1, 5), E("b", 1, 5), E("c", 1, 5)]


def test_full_mix():
    events = [
        E("alice", 2, 100),
        E("bob",   1, 200),
        E("alice", 1, 200),
        E("bob",   1, 100),
    ]
    assert ex.sort_events(events) == [
        E("bob",   1, 100),
        E("alice", 1, 200),
        E("bob",   1, 200),
        E("alice", 2, 100),
    ]


def test_empty():
    assert ex.sort_events([]) == []
