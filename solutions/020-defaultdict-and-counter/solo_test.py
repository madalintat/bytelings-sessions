"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_equal():
    assert ex.letter_diff("abc", "abc") == {}


def test_a_has_more():
    assert ex.letter_diff("aabc", "abc") == {"a": 1}


def test_b_has_more():
    assert ex.letter_diff("abc", "aabc") == {"a": -1}


def test_both_empty():
    assert ex.letter_diff("", "") == {}


def test_one_empty():
    assert ex.letter_diff("abc", "") == {"a": 1, "b": 1, "c": 1}
    assert ex.letter_diff("", "abc") == {"a": -1, "b": -1, "c": -1}


def test_hello_world():
    out = ex.letter_diff("hello", "world")
    # 'l' appears 2 in hello, 1 in world -> +1; 'h':1 only in hello; 'e':1; 'o' equal
    # 'w':1 only in world -> -1; 'r':1; 'd':1
    expected = {"h": 1, "e": 1, "l": 1, "w": -1, "r": -1, "d": -1}
    assert out == expected


def test_case_sensitive():
    assert ex.letter_diff("aA", "aa") == {"A": 1, "a": -1}


def test_anagram_returns_empty():
    assert ex.letter_diff("listen", "silent") == {}
