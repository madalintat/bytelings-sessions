"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_has_value_distinguishes_empty_from_none():
    assert ex.has_value("") is True   # empty string is *a* value
    assert ex.has_value(None) is False
    assert ex.has_value(0) is True    # zero is *a* value
    assert ex.has_value("hi") is True


def test_is_blank_string():
    assert ex.is_blank_string("") is True
    assert ex.is_blank_string("a") is False


def test_is_definitely_false():
    assert ex.is_definitely_false(False) is True
    assert ex.is_definitely_false(0) is False     # 0 == False but 0 is not False
    assert ex.is_definitely_false(None) is False
    assert ex.is_definitely_false("") is False
