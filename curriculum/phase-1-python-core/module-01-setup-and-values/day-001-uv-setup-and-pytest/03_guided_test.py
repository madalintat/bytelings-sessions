"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_zero_is_even():
    assert ex.is_even(0) is True


def test_two_is_even():
    assert ex.is_even(2) is True


def test_seven_is_odd():
    assert ex.is_even(7) is False


def test_negative_even():
    assert ex.is_even(-4) is True


def test_negative_odd():
    assert ex.is_even(-3) is False


def test_returns_bool_not_int():
    """is_even must return True/False, not 1/0 — modulo gives int!"""
    result = ex.is_even(4)
    assert result is True or result is False
