"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_none_returns_fallback():
    assert ex.default_if_none(None, "x") == "x"


def test_empty_string_returns_empty_string():
    assert ex.default_if_none("", "x") == ""


def test_zero_returns_zero():
    assert ex.default_if_none(0, 99) == 0


def test_value_returns_value():
    assert ex.default_if_none("hello", "x") == "hello"
