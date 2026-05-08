"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_sorted_copy_returns_sorted():
    assert ex.sorted_copy([3, 1, 2]) == [1, 2, 3]


def test_sorted_copy_does_not_mutate():
    src = [3, 1, 2]
    ex.sorted_copy(src)
    assert src == [3, 1, 2]


def test_sorted_copy_empty():
    assert ex.sorted_copy([]) == []


def test_reversed_copy_returns_reversed():
    assert ex.reversed_copy([1, 2, 3]) == [3, 2, 1]


def test_reversed_copy_does_not_mutate():
    src = [1, 2, 3]
    ex.reversed_copy(src)
    assert src == [1, 2, 3]


def test_remove_evens_basic():
    assert ex.remove_evens([1, 2, 3, 4, 5, 6]) == [1, 3, 5]


def test_remove_evens_does_not_mutate():
    src = [1, 2, 3, 4]
    ex.remove_evens(src)
    assert src == [1, 2, 3, 4]


def test_remove_evens_all_evens():
    assert ex.remove_evens([2, 4, 6]) == []
