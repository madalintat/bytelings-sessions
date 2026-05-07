"""Tests for rung 2 — fill in the Big-O strings."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_first_item_is_constant():
    assert ex.BIGO_FIRST_ITEM == "O(1)"


def test_sum_items_is_linear():
    assert ex.BIGO_SUM_ITEMS == "O(n)"


def test_has_pair_naive_is_quadratic():
    assert ex.BIGO_HAS_PAIR_NAIVE == "O(n^2)"


def test_sort_is_n_log_n():
    assert ex.BIGO_SORT == "O(n log n)"


def test_functions_still_work():
    assert ex.first_item([1, 2, 3]) == 1
    assert ex.sum_items([1, 2, 3]) == 6
    assert ex.has_pair_naive([1, 2, 3, 4], 5) is True
    assert ex.has_pair_naive([1, 2, 3], 100) is False
    assert ex.my_sort([3, 1, 2]) == [1, 2, 3]
