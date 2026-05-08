"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.min_coins([1, 2, 5], 11) == 3


def test_impossible():
    assert ex.min_coins([2], 3) == -1


def test_zero():
    assert ex.min_coins([1, 2, 5], 0) == 0


def test_one_coin_kind():
    assert ex.min_coins([5], 25) == 5


def test_greedy_would_fail():
    """Greedy from the largest fails: 6+1+1+1+1=5 coins; 4+4+1=3 is best."""
    assert ex.min_coins([1, 4, 6], 9) == 3


def test_large_amount():
    assert ex.min_coins([1, 5, 10, 25], 73) == 7


def test_amount_one():
    assert ex.min_coins([1, 5, 10], 1) == 1
