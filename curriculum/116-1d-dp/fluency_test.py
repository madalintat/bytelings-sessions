"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_all_positive():
    assert ex.max_subarray([1, 2, 3, 4]) == 10


def test_all_negative():
    assert ex.max_subarray([-3, -1, -7]) == -1


def test_one():
    assert ex.max_subarray([5]) == 5


def test_one_negative():
    assert ex.max_subarray([-5]) == -5


def test_leading_negative():
    """The bug: a leading negative ruins fresh-start cases."""
    assert ex.max_subarray([-100, 5, 3]) == 8


def test_empty():
    assert ex.max_subarray([]) == 0
