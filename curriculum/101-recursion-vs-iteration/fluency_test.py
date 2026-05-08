"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_max_basic():
    assert ex.max_in_list([3, 1, 4, 1, 5, 9, 2, 6]) == 9


def test_max_single():
    assert ex.max_in_list([42]) == 42


def test_max_negatives():
    assert ex.max_in_list([-3, -1, -7]) == -1


def test_max_long_no_recursion_error():
    """Iterative rewrite must handle 5000 ints without RecursionError."""
    big = list(range(5000))
    assert ex.max_in_list(big) == 4999


def test_flatten_flat():
    assert ex.flatten([1, 2, 3]) == [1, 2, 3]


def test_flatten_one_level():
    assert ex.flatten([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_flatten_deep():
    assert ex.flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]


def test_flatten_empty():
    assert ex.flatten([]) == []
