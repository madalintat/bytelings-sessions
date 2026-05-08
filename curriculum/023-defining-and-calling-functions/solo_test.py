"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.parse_flags([]) == {"verbose": False, "out": None, "count": None}


def test_verbose_only():
    assert ex.parse_flags(["--verbose"]) == {
        "verbose": True, "out": None, "count": None
    }


def test_out_equals_form():
    assert ex.parse_flags(["--out=x.txt"]) == {
        "verbose": False, "out": "x.txt", "count": None
    }


def test_out_space_form():
    assert ex.parse_flags(["--out", "x.txt"]) == {
        "verbose": False, "out": "x.txt", "count": None
    }


def test_count_int():
    assert ex.parse_flags(["--count", "3"]) == {
        "verbose": False, "out": None, "count": 3
    }


def test_combined():
    assert ex.parse_flags(["--verbose", "--out=x", "--count", "7"]) == {
        "verbose": True, "out": "x", "count": 7
    }


def test_unknown_flag_raises():
    with pytest.raises(ValueError):
        ex.parse_flags(["--bogus"])


def test_unknown_flag_ignored():
    assert ex.parse_flags(["--bogus"], allow_unknown=True) == {
        "verbose": False, "out": None, "count": None
    }


def test_count_non_int_raises():
    with pytest.raises(ValueError):
        ex.parse_flags(["--count", "abc"])


def test_out_missing_value_raises():
    with pytest.raises(ValueError):
        ex.parse_flags(["--out"])
