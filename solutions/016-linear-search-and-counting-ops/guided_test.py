"""Tests for rung 3."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.argmax([3, 1, 4, 1, 5, 9, 2, 6]) == 5


def test_tie_smallest_index():
    assert ex.argmax([1, 1, 1]) == 0


def test_with_key():
    assert ex.argmax(["bee", "a", "carrot"], key=len) == 2


def test_with_key_tie():
    assert ex.argmax(["aa", "bb"], key=len) == 0


def test_single_element():
    assert ex.argmax([42]) == 0


def test_empty_raises():
    with pytest.raises(ValueError):
        ex.argmax([])


def test_negative_numbers():
    assert ex.argmax([-3, -1, -7]) == 1
