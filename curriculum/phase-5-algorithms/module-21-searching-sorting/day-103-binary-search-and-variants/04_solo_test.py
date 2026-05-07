"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.max_requests([1, 2, 3, 4, 5], 6) == 3


def test_none_fit():
    assert ex.max_requests([10, 20, 30], 5) == 0


def test_all_fit():
    assert ex.max_requests([1, 1, 1, 1], 100) == 4


def test_exact():
    assert ex.max_requests([1, 2, 3], 6) == 3


def test_just_under():
    assert ex.max_requests([1, 2, 3], 5) == 2


def test_empty():
    assert ex.max_requests([], 100) == 0


def test_zero_capacity():
    assert ex.max_requests([1, 2, 3], 0) == 0


def test_large_input():
    costs = [1] * 10000
    assert ex.max_requests(costs, 7500) == 7500
