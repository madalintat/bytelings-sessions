"""Tests for rung 2 — behavior + structural."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


# behavior
def test_indexed_basic():
    assert ex.indexed(["a", "b", "c"]) == [(0, "a"), (1, "b"), (2, "c")]


def test_indexed_empty():
    assert ex.indexed([]) == []


def test_squares_basic():
    assert ex.squares([1, 2, 3]) == [1, 4, 9]


def test_is_empty():
    assert ex.is_empty("") is True
    assert ex.is_empty("hello") is False


# structural
def test_indexed_uses_enumerate():
    src = inspect.getsource(ex.indexed)
    assert "enumerate" in src, "use enumerate(items)"
    assert "range(len(" not in src, "drop the range(len(...)) idiom"


def test_squares_uses_comprehension():
    src = inspect.getsource(ex.squares)
    assert "[" in src and " for " in src, "use a list comprehension"
    assert ".append" not in src, "drop the .append loop"


def test_is_empty_uses_truthiness():
    src = inspect.getsource(ex.is_empty)
    assert '== ""' not in src, 'use truthiness, not == ""'
