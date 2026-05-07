"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_division():
    assert ex.safe_divide(10, 2) == 5.0


def test_division_by_zero_returns_none():
    assert ex.safe_divide(10, 0) is None


def test_negative():
    assert ex.safe_divide(-10, 2) == -5.0


def test_returns_float_not_int():
    assert isinstance(ex.safe_divide(4, 2), float)
