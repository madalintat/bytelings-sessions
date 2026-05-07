"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _check_both(houses, expected):
    assert ex.rob_topdown(houses) == expected
    assert ex.rob_bottomup(houses) == expected


def test_basic():
    _check_both([2, 7, 9, 3, 1], 12)


def test_two_houses():
    _check_both([1, 2], 2)


def test_one_house():
    _check_both([5], 5)


def test_empty():
    _check_both([], 0)


def test_decreasing():
    _check_both([5, 1, 1, 5], 10)


def test_all_zero():
    _check_both([0, 0, 0, 0], 0)
