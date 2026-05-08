"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_is_palindrome():
    assert ex.is_palindrome("") is True


def test_single_is_palindrome():
    assert ex.is_palindrome("a") is True


def test_two_same():
    assert ex.is_palindrome("aa") is True


def test_two_different():
    assert ex.is_palindrome("ab") is False


def test_odd_length_palindrome():
    assert ex.is_palindrome("racecar") is True


def test_even_length_palindrome():
    assert ex.is_palindrome("abba") is True


def test_not_palindrome():
    assert ex.is_palindrome("hello") is False


def test_case_sensitive():
    assert ex.is_palindrome("Aa") is False
