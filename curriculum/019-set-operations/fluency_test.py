"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_unique_items_basic():
    assert ex.unique_items([1, 2, 1, 3, 2]) == {1, 2, 3}


def test_unique_items_empty():
    assert ex.unique_items([]) == set()
    assert isinstance(ex.unique_items([]), set)


def test_in_both_basic():
    assert ex.in_both([1, 2, 3], [2, 3, 4]) == {2, 3}


def test_in_both_disjoint():
    assert ex.in_both([1, 2], [3, 4]) == set()


def test_in_a_only():
    assert ex.in_a_only({1, 2, 3, 4}, {3, 4, 5}) == {1, 2}


def test_in_a_only_empty_b():
    assert ex.in_a_only({1, 2}, set()) == {1, 2}


def test_first_repeat_basic():
    assert ex.first_repeat([1, 2, 3, 2, 1]) == 2


def test_first_repeat_none():
    assert ex.first_repeat([1, 2, 3]) is None


def test_first_repeat_empty():
    assert ex.first_repeat([]) is None
