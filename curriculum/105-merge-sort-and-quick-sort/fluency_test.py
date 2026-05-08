"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_one_empty():
    assert ex.merge([], [1, 2, 3]) == [1, 2, 3]
    assert ex.merge([1, 2, 3], []) == [1, 2, 3]


def test_unequal_lengths():
    assert ex.merge([1, 2], [3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert ex.merge([1, 2, 3, 4, 5], [6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_interleaved():
    assert ex.merge([1, 4, 7], [2, 3, 8]) == [1, 2, 3, 4, 7, 8]


def test_dupes():
    assert ex.merge([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_both_empty():
    assert ex.merge([], []) == []
