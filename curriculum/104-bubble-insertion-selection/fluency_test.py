"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_empty():
    assert ex.bubble_sort([]) == []


def test_one():
    assert ex.bubble_sort([42]) == [42]


def test_already_sorted():
    assert ex.bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse():
    assert ex.bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_does_not_mutate_input():
    src = [3, 1, 2]
    _ = ex.bubble_sort(src)
    assert src == [3, 1, 2]
