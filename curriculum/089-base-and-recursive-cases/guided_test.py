"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.nested_sum([]) == 0


def test_flat():
    assert ex.nested_sum([1, 2, 3]) == 6


def test_one_level():
    assert ex.nested_sum([1, [2, 3], 4]) == 10


def test_deep():
    assert ex.nested_sum([1, [2, [3, [4, [5]]]]]) == 15


def test_only_nested():
    assert ex.nested_sum([[[[7]]]]) == 7


def test_negative_numbers():
    assert ex.nested_sum([-1, [2, [-3]], 4]) == 2


def test_empty_inside():
    assert ex.nested_sum([[], [1], [[]], [[2]]]) == 3
