"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.is_palindrome("") is True


def test_single_char():
    assert ex.is_palindrome("a") is True


def test_simple_yes():
    assert ex.is_palindrome("racecar") is True


def test_simple_no():
    assert ex.is_palindrome("hello") is False


def test_case_insensitive():
    assert ex.is_palindrome("Racecar") is True
    assert ex.is_palindrome("RaceCar") is True


def test_with_punctuation():
    assert ex.is_palindrome("A man, a plan, a canal: Panama") is True


def test_almost_palindrome():
    assert ex.is_palindrome("racecars") is False


def test_numbers_count():
    assert ex.is_palindrome("12321") is True
    assert ex.is_palindrome("12345") is False
