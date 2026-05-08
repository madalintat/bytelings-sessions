"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _check_both(arr):
    expected = sorted(arr)
    src = list(arr)
    assert ex.selection_sort(arr) == expected
    assert arr == src, "selection_sort mutated input"
    assert ex.insertion_sort(arr) == expected
    assert arr == src, "insertion_sort mutated input"


def test_basic():
    _check_both([3, 1, 4, 1, 5, 9, 2, 6])


def test_empty():
    _check_both([])


def test_one():
    _check_both([42])


def test_sorted():
    _check_both([1, 2, 3, 4, 5])


def test_reverse():
    _check_both([5, 4, 3, 2, 1])


def test_dupes():
    _check_both([2, 2, 2, 1, 1, 3])


def test_negatives():
    _check_both([0, -1, -5, 3, -2])
