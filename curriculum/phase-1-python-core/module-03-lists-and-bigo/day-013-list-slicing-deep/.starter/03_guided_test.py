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
    assert ex.chunks([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]


def test_empty():
    assert ex.chunks([], 3) == []


def test_smaller_than_chunk():
    assert ex.chunks([1, 2], 5) == [[1, 2]]


def test_exact_multiple():
    assert ex.chunks([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_size_one():
    assert ex.chunks([1, 2, 3], 1) == [[1], [2], [3]]


def test_invalid_size():
    with pytest.raises(ValueError):
        ex.chunks([1, 2, 3], 0)
    with pytest.raises(ValueError):
        ex.chunks([1, 2, 3], -1)


def test_does_not_mutate():
    src = [1, 2, 3, 4]
    ex.chunks(src, 2)
    assert src == [1, 2, 3, 4]
