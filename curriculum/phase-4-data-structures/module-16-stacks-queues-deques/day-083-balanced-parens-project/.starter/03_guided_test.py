"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_balanced_returns_none():
    assert ex.check_brackets("(())") is None


def test_empty_returns_none():
    assert ex.check_brackets("") is None


def test_no_brackets_returns_none():
    assert ex.check_brackets("hello world") is None


def test_mixed_balanced():
    assert ex.check_brackets("(a[b]{c})") is None


def test_stray_closer():
    p = ex.check_brackets("ab)cd")
    assert p is not None
    assert p.kind == "stray-closer"
    assert p.index == 2
    assert p.char == ")"


def test_mismatched():
    p = ex.check_brackets("([)]")
    assert p is not None
    assert p.kind == "mismatched"
    assert p.index == 2
    assert p.char == ")"


def test_unclosed_simple():
    p = ex.check_brackets("([")
    assert p is not None
    assert p.kind == "unclosed"
    assert p.index == 1
    assert p.char == "["


def test_unclosed_after_balanced():
    # the "(" at index 5 stays open
    p = ex.check_brackets("(())(a")
    assert p is not None
    assert p.kind == "unclosed"
    assert p.index == 4
    assert p.char == "("


def test_first_problem_wins():
    # there's an unclosed AND a mismatch; the mismatch comes first.
    p = ex.check_brackets("(]{")
    assert p is not None
    assert p.kind == "mismatched"
    assert p.index == 1
