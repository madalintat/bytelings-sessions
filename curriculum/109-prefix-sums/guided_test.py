"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.count_subarrays_with_sum([1, 1, 1], 2) == 2


def test_with_negatives():
    assert ex.count_subarrays_with_sum([1, -1, 1, -1], 0) == 4


def test_target_3():
    assert ex.count_subarrays_with_sum([1, 2, 3], 3) == 2


def test_no_match():
    assert ex.count_subarrays_with_sum([1, 2, 3], 100) == 0


def test_empty():
    assert ex.count_subarrays_with_sum([], 0) == 0


def test_zero_target_with_zeros():
    assert ex.count_subarrays_with_sum([0, 0, 0], 0) == 6
