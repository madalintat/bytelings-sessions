"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_behavior():
    assert ex.mystery([1, 1, 2, 3, 3, 3, 2]) == [1, 2, 3, 2]


def test_already_dedup():
    assert ex.mystery([1, 2, 3]) == [1, 2, 3]


def test_empty():
    assert ex.mystery([]) == []


def test_all_same():
    assert ex.mystery([5, 5, 5, 5]) == [5]


def test_docstring_present():
    assert ex.mystery.__doc__ is not None, "add a docstring describing the function"
    doc = ex.mystery.__doc__.lower()
    assert "consecutive" in doc, (
        "the docstring should mention 'consecutive' — that's the key insight "
        "(it removes only adjacent duplicates, not all duplicates)"
    )
