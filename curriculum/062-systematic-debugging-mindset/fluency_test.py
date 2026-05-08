"""Tests for rung 2.

The first three tests already pass (the bug doesn't show with these
inputs). The fourth `test_regression_for_overdiscount` is what locks
in the fix. Implement the function AND ensure that test passes.
"""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_normal_discount():
    assert ex.apply_discount(1000, 200) == 800


def test_zero_discount():
    assert ex.apply_discount(1000, 0) == 1000


def test_full_discount():
    assert ex.apply_discount(1000, 1000) == 0


def test_regression_for_overdiscount():
    """The bug: discount > price returned a negative number. Lock it in."""
    assert ex.apply_discount(1000, 1500) == 0
    assert ex.apply_discount(0, 100) == 0
