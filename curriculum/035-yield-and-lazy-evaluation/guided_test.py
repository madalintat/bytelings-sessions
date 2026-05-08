"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert list(ex.chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_exact_multiple():
    assert list(ex.chunked([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_chunk_larger_than_input():
    assert list(ex.chunked([1, 2], 5)) == [[1, 2]]


def test_empty():
    assert list(ex.chunked([], 3)) == []


def test_size_zero_raises():
    with pytest.raises(ValueError):
        list(ex.chunked([1, 2], 0))


def test_size_negative_raises():
    with pytest.raises(ValueError):
        list(ex.chunked([1, 2], -1))


def test_works_on_any_iterable():
    assert list(ex.chunked((x for x in range(5)), 2)) == [[0, 1], [2, 3], [4]]
