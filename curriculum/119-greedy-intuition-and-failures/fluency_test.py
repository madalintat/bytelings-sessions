"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    meetings = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 9)]
    assert ex.max_meetings(meetings) == 3


def test_empty():
    assert ex.max_meetings([]) == 0


def test_one():
    assert ex.max_meetings([(0, 5)]) == 1


def test_all_overlap():
    meetings = [(0, 10), (1, 11), (2, 12)]
    assert ex.max_meetings(meetings) == 1


def test_back_to_back():
    meetings = [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert ex.max_meetings(meetings) == 4


def test_sort_by_start_would_fail():
    """The classic counterexample to sort-by-start: a long greedy meeting
    blocks several short ones."""
    meetings = [(0, 100), (1, 2), (2, 3), (3, 4)]
    assert ex.max_meetings(meetings) == 3
