"""Tests for rung 2 — should be green after the TODOs are fixed."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_first_char():
    assert ex.first_char("panopticon") == "p"
    assert ex.first_char("a") == "a"


def test_last_char():
    assert ex.last_char("panopticon") == "n"
    assert ex.last_char("z") == "z"


def test_middle_three():
    assert ex.middle_three("panopticon") == "nop"
    assert ex.middle_three("abcdef") == "cde"


def test_reversed_str():
    assert ex.reversed_str("hello") == "olleh"
    assert ex.reversed_str("") == ""
    assert ex.reversed_str("a") == "a"
