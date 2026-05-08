"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.every_other("abcdef") == "ace"


def test_empty():
    assert ex.every_other("") == ""


def test_single_char():
    assert ex.every_other("x") == "x"


def test_two_chars():
    assert ex.every_other("ab") == "a"


def test_long():
    assert ex.every_other("panopticon") == "pnpio"


def test_returns_string():
    assert isinstance(ex.every_other("hello"), str)
