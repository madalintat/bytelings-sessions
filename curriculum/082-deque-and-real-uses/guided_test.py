"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_last_n_basic():
    assert ex.last_n([1, 2, 3, 4, 5], 3) == [3, 4, 5]


def test_last_n_short_stream():
    assert ex.last_n([1, 2], 5) == [1, 2]


def test_last_n_string():
    assert ex.last_n("abcde", 2) == ["d", "e"]


def test_last_n_zero():
    assert ex.last_n([1, 2, 3], 0) == []


def test_last_n_works_with_iterator():
    """Must accept any iterable, not just list/tuple."""
    assert ex.last_n(iter(range(100)), 3) == [97, 98, 99]


def test_rolling_max_basic():
    assert ex.rolling_max([1, 3, 2, 5, 4], 3) == [3, 5, 5]


def test_rolling_max_k_equals_one():
    assert ex.rolling_max([7, 2, 9, 1], 1) == [7, 2, 9, 1]


def test_rolling_max_empty():
    assert ex.rolling_max([], 3) == []


def test_rolling_max_full_window():
    assert ex.rolling_max([4, 1, 3], 3) == [4]
