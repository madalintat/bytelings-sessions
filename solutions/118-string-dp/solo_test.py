"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _is_palindrome(s):
    return s == s[::-1]


def test_basic():
    out = ex.longest_palindrome("babad")
    assert _is_palindrome(out) and out in {"bab", "aba"}


def test_even():
    assert ex.longest_palindrome("cbbd") == "bb"


def test_single():
    assert ex.longest_palindrome("a") == "a"


def test_empty():
    assert ex.longest_palindrome("") == ""


def test_full_palindrome():
    assert ex.longest_palindrome("racecar") == "racecar"


def test_all_same():
    assert ex.longest_palindrome("aaaa") == "aaaa"


def test_no_long_palindrome():
    out = ex.longest_palindrome("abcde")
    assert _is_palindrome(out)
    assert len(out) == 1


def test_long_input():
    s = "forgeeksskeegfor"
    out = ex.longest_palindrome(s)
    assert _is_palindrome(out)
    assert len(out) == 10   # "geeksskeeg"
