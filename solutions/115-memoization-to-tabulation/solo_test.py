"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.min_path([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11


def test_one_row():
    assert ex.min_path([[7]]) == 7


def test_two_rows():
    assert ex.min_path([[1], [2, 3]]) == 3


def test_negatives():
    assert ex.min_path([[-1], [2, 3], [1, -1, -3]]) == -5


def test_all_zero():
    assert ex.min_path([[0], [0, 0], [0, 0, 0]]) == 0


def test_straight_path():
    # forced path
    tri = [[1], [10, 1], [10, 10, 1]]
    assert ex.min_path(tri) == 3
