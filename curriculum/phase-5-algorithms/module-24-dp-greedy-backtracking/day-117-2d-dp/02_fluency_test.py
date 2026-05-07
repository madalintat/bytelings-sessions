"""Tests for rung 2.

Note: unique_paths(m, n) is symmetric — paths(m, n) == paths(n, m).
The fill-order bug shows when m != n.
"""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_3x7():
    assert ex.unique_paths(3, 7) == 28


def test_2x2():
    assert ex.unique_paths(2, 2) == 2


def test_1x_anything():
    assert ex.unique_paths(1, 7) == 1


def test_anything_x1():
    assert ex.unique_paths(7, 1) == 1


def test_zero():
    assert ex.unique_paths(0, 5) == 0
    assert ex.unique_paths(5, 0) == 0


def test_4x5():
    assert ex.unique_paths(4, 5) == 35
