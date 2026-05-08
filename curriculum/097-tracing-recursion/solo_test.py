"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.reverse("") == ""


def test_one_char():
    assert ex.reverse("a") == "a"


def test_basic():
    assert ex.reverse("abc") == "cba"


def test_palindrome():
    assert ex.reverse("racecar") == "racecar"


def test_with_space():
    assert ex.reverse("hello world") == "dlrow olleh"


def test_unicode():
    assert ex.reverse("café") == "éfac"
