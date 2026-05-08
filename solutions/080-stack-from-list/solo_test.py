"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.reverse_string("") == ""


def test_single_char():
    assert ex.reverse_string("a") == "a"


def test_basic():
    assert ex.reverse_string("hello") == "olleh"


def test_palindrome_unchanged():
    assert ex.reverse_string("racecar") == "racecar"


def test_with_spaces():
    assert ex.reverse_string("ab cd") == "dc ba"


def test_long():
    s = "the quick brown fox"
    assert ex.reverse_string(s) == s[::-1]
