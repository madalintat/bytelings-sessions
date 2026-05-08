"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.sum_iterative([1, 2, 3, 4, 5]) == 15


def test_empty():
    assert ex.sum_iterative([]) == 0


def test_one():
    assert ex.sum_iterative([42]) == 42


def test_long_input_does_not_recurse():
    """The whole point: 5000 elements without RecursionError."""
    big = list(range(5000))
    assert ex.sum_iterative(big) == sum(big)


def test_negatives():
    assert ex.sum_iterative([-1, -2, -3]) == -6
