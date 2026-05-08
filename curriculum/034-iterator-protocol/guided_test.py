"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert list(ex.Squares(4)) == [0, 1, 4, 9]


def test_zero():
    assert list(ex.Squares(0)) == []


def test_one():
    assert list(ex.Squares(1)) == [0]


def test_works_in_sum():
    assert sum(ex.Squares(5)) == 0 + 1 + 4 + 9 + 16


def test_unpacking():
    a, b, c = ex.Squares(3)
    assert (a, b, c) == (0, 1, 4)


def test_iter_returns_self():
    s = ex.Squares(3)
    assert iter(s) is s
