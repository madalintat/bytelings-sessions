"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_zero():
    assert ex.digit_sum(0) == 0


def test_single_digit():
    assert ex.digit_sum(7) == 7


def test_two_digits():
    assert ex.digit_sum(42) == 6


def test_three_digits():
    assert ex.digit_sum(123) == 6


def test_all_nines():
    assert ex.digit_sum(999) == 27


def test_large_number():
    assert ex.digit_sum(1_000_000) == 1
