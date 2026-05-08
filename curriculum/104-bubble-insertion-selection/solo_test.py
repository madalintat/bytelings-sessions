"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    out, cmps = ex.insertion_sort_with_stats([])
    assert out == []
    assert cmps == 0


def test_single():
    out, cmps = ex.insertion_sort_with_stats([7])
    assert out == [7]
    assert cmps == 0


def test_sorted_best_case():
    out, cmps = ex.insertion_sort_with_stats([1, 2, 3, 4])
    assert out == [1, 2, 3, 4]
    # Best case: each new element compared once against its left neighbor.
    assert cmps == 3


def test_reverse_worst_case():
    out, cmps = ex.insertion_sort_with_stats([4, 3, 2, 1])
    assert out == [1, 2, 3, 4]
    # Worst case: 1 + 2 + 3 = 6 comparisons.
    assert cmps == 6


def test_random():
    out, cmps = ex.insertion_sort_with_stats([3, 1, 4, 1, 5, 9, 2, 6])
    assert out == [1, 1, 2, 3, 4, 5, 6, 9]
    assert cmps > 0
