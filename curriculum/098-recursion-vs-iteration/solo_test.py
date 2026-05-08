"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_gcd_basic():
    assert ex.gcd(12, 8) == 4
    assert ex.gcd(100, 75) == 25


def test_gcd_coprime():
    assert ex.gcd(7, 13) == 1


def test_gcd_equal():
    assert ex.gcd(9, 9) == 9


def test_gcd_one():
    assert ex.gcd(1, 99) == 1


def test_gcd_with_zero():
    assert ex.gcd(15, 0) == 15


def test_running_sum_empty():
    assert ex.running_sum([]) == []


def test_running_sum_basic():
    assert ex.running_sum([3, 1, 4, 1, 5]) == [3, 4, 8, 9, 14]


def test_running_sum_one():
    assert ex.running_sum([7]) == [7]


def test_running_sum_negatives():
    assert ex.running_sum([1, -1, 2, -2]) == [1, 0, 2, 0]
