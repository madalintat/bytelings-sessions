"""HIDDEN tests for rung 4."""
import importlib.util
import random
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.top_k([5, 1, 9, 3, 7, 2], 3) == [9, 7, 5]


def test_k_zero():
    assert ex.top_k([1, 2, 3], 0) == []


def test_empty_stream():
    assert ex.top_k([], 3) == []


def test_k_larger_than_stream():
    assert ex.top_k([1, 2], 5) == [2, 1]


def test_iterators_work():
    assert ex.top_k(iter([5, 1, 9, 3, 7, 2]), 2) == [9, 7]


def test_with_duplicates():
    assert ex.top_k([5, 5, 5, 1, 1], 3) == [5, 5, 5]


def test_large_random():
    rnd = random.Random(0)
    nums = [rnd.randint(-10_000, 10_000) for _ in range(2000)]
    expected = sorted(nums, reverse=True)[:50]
    assert ex.top_k(nums, 50) == expected
