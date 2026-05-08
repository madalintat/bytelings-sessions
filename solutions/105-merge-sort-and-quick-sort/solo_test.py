"""HIDDEN tests for rung 4."""
import importlib.util
import random
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.quick_sort([]) == []


def test_one():
    assert ex.quick_sort([7]) == [7]


def test_basic():
    assert ex.quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_already_sorted():
    """Quicksort with middle pivot should not crash on sorted input."""
    arr = list(range(50))
    assert ex.quick_sort(arr) == arr


def test_reverse():
    assert ex.quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_dupes():
    assert ex.quick_sort([2, 2, 2, 1, 1, 3]) == [1, 1, 2, 2, 2, 3]


def test_does_not_mutate():
    src = [3, 1, 2]
    _ = ex.quick_sort(src)
    assert src == [3, 1, 2]


def test_random_large():
    random.seed(7)
    arr = [random.randint(-100, 100) for _ in range(300)]
    assert ex.quick_sort(arr) == sorted(arr)
