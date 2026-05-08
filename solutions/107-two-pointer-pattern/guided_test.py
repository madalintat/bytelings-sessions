"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.pair_sum([1, 2, 4, 7, 11], 9) == (1, 3)


def test_first_and_last():
    assert ex.pair_sum([1, 2, 3, 4, 5], 6) in {(0, 4), (1, 3)}


def test_no_pair():
    assert ex.pair_sum([1, 2, 3, 4, 5], 100) is None


def test_negative_target():
    assert ex.pair_sum([-3, -1, 2, 4], 1) == (1, 2)


def test_empty():
    assert ex.pair_sum([], 5) is None


def test_one():
    assert ex.pair_sum([5], 10) is None


def test_two_exactly():
    assert ex.pair_sum([3, 7], 10) == (0, 1)
