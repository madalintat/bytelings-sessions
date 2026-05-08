"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_simple_balanced():
    assert ex.is_balanced_simple("(())") is True


def test_simple_empty():
    assert ex.is_balanced_simple("") is True


def test_simple_unbalanced_extra_close():
    assert ex.is_balanced_simple(")(") is False


def test_simple_unbalanced_unclosed():
    assert ex.is_balanced_simple("(()") is False


def test_simple_ignores_other_chars():
    assert ex.is_balanced_simple("a(b)c(d)") is True


def test_matches_paren():
    assert ex.matches("(", ")") is True


def test_matches_square():
    assert ex.matches("[", "]") is True


def test_matches_curly():
    assert ex.matches("{", "}") is True


def test_matches_mismatched():
    assert ex.matches("(", "]") is False


def test_matches_garbage():
    assert ex.matches("a", "b") is False
