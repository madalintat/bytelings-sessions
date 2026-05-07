"""Tests for rung 3."""
import importlib.util
import random
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.merge_sort([]) == []


def test_one():
    assert ex.merge_sort([42]) == [42]


def test_basic():
    assert ex.merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_sorted():
    assert ex.merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse():
    assert ex.merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_does_not_mutate():
    src = [3, 1, 2]
    _ = ex.merge_sort(src)
    assert src == [3, 1, 2]


def test_random_large():
    random.seed(42)
    arr = [random.randint(-1000, 1000) for _ in range(500)]
    assert ex.merge_sort(arr) == sorted(arr)
