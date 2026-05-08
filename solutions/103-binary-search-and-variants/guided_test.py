"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_lower_basic():
    assert ex.lower_bound([1, 2, 4, 4, 4, 6], 4) == 2


def test_lower_missing_returns_insertion_point():
    assert ex.lower_bound([1, 2, 4, 4, 4, 6], 3) == 2
    assert ex.lower_bound([1, 2, 4, 4, 4, 6], 5) == 5


def test_lower_first():
    assert ex.lower_bound([1, 2, 3], 0) == 0


def test_lower_after_last():
    assert ex.lower_bound([1, 2, 3], 99) == 3


def test_lower_empty():
    assert ex.lower_bound([], 5) == 0


def test_upper_basic():
    assert ex.upper_bound([1, 2, 4, 4, 4, 6], 4) == 5


def test_upper_missing():
    assert ex.upper_bound([1, 2, 4, 4, 4, 6], 3) == 2
    assert ex.upper_bound([1, 2, 4, 4, 4, 6], 5) == 5


def test_upper_after_last():
    assert ex.upper_bound([1, 2, 3], 99) == 3


def test_count_duplicates():
    arr = [1, 2, 4, 4, 4, 6]
    assert ex.upper_bound(arr, 4) - ex.lower_bound(arr, 4) == 3
