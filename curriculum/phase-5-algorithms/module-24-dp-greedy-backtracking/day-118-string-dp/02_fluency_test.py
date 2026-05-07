"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_yes():
    assert ex.can_segment("leetcode", ["leet", "code"]) is True


def test_basic_no():
    assert ex.can_segment("apple", ["app", "le", "lea"]) is False


def test_apples():
    assert ex.can_segment("applepenapple", ["apple", "pen"]) is True


def test_empty_string():
    assert ex.can_segment("", ["a"]) is True


def test_single_letter():
    assert ex.can_segment("a", ["a"]) is True


def test_must_be_fast():
    """Without memoization this hangs. With @cache, it's instant."""
    s = "a" * 30 + "b"
    assert ex.can_segment(s, ["a", "aa", "aaa", "aaaa"]) is False
