"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_canonical():
    assert ex.largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]) == 10


def test_two_bars():
    assert ex.largest_rectangle_in_histogram([2, 4]) == 4


def test_single():
    assert ex.largest_rectangle_in_histogram([5]) == 5


def test_empty():
    assert ex.largest_rectangle_in_histogram([]) == 0


def test_descending():
    assert ex.largest_rectangle_in_histogram([5, 4, 3, 2, 1]) == 9


def test_ascending():
    assert ex.largest_rectangle_in_histogram([1, 2, 3, 4, 5]) == 9


def test_all_equal():
    assert ex.largest_rectangle_in_histogram([3, 3, 3, 3]) == 12


def test_valley():
    assert ex.largest_rectangle_in_histogram([3, 1, 3]) == 3


def test_tall_narrow():
    assert ex.largest_rectangle_in_histogram([0, 9, 0]) == 9
