"""Tests for rung 2."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_smallest_basic():
    assert ex.smallest([5, 1, 9, 3, 7, 2]) == 1


def test_smallest_negatives():
    assert ex.smallest([-3, -10, -1, 0]) == -10


def test_smallest_empty_raises():
    with pytest.raises(IndexError):
        ex.smallest([])


def test_largest_three_basic():
    assert ex.largest_three([5, 1, 9, 3, 7, 2]) == [9, 7, 5]


def test_largest_three_with_ties():
    # ties allowed — both 9s show up
    assert ex.largest_three([9, 9, 1]) == [9, 9, 1]


def test_largest_three_short_list():
    assert ex.largest_three([5, 2]) == [5, 2]


def test_largest_three_empty():
    assert ex.largest_three([]) == []
