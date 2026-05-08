"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_classic():
    assert ex.lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_empty():
    assert ex.lis([]) == 0


def test_already_sorted():
    assert ex.lis([1, 2, 3, 4, 5]) == 5


def test_all_equal():
    assert ex.lis([5, 5, 5]) == 1


def test_decreasing():
    assert ex.lis([5, 4, 3, 2, 1]) == 1


def test_with_dupes():
    assert ex.lis([1, 2, 2, 3]) == 3


def test_one():
    assert ex.lis([7]) == 1
