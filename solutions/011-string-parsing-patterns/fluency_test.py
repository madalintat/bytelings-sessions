"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_csv_fields_basic():
    assert ex.csv_fields("a, b , c") == ["a", "b", "c"]


def test_csv_fields_no_spaces():
    assert ex.csv_fields("a,b,c") == ["a", "b", "c"]


def test_csv_fields_empty():
    assert ex.csv_fields("") == [""]


def test_keep_digits_basic():
    assert ex.keep_digits("a1b2c3") == "123"


def test_keep_digits_phone():
    assert ex.keep_digits("+1 (415) 555-1212") == "14155551212"


def test_keep_digits_none():
    assert ex.keep_digits("abc") == ""


def test_split_on_any_two_seps():
    assert ex.split_on_any("a, b; c", ",;") == ["a", "b", "c"]


def test_split_on_any_drops_empty():
    assert ex.split_on_any(",,a;,;b", ",;") == ["a", "b"]


def test_split_on_any_no_seps_in_string():
    assert ex.split_on_any("hello", ",;") == ["hello"]
