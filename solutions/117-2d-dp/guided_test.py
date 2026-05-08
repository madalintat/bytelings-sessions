"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7


def test_single():
    assert ex.min_path_sum([[5]]) == 5


def test_one_row():
    assert ex.min_path_sum([[1, 2, 3]]) == 6


def test_one_col():
    assert ex.min_path_sum([[1], [2], [3]]) == 6


def test_empty():
    assert ex.min_path_sum([]) == 0


def test_zeros():
    assert ex.min_path_sum([[0, 0], [0, 0]]) == 0


def test_2x2():
    assert ex.min_path_sum([[1, 2], [1, 1]]) == 3
