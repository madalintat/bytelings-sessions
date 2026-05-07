"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_build():
    assert ex.build_prefix([3, 1, 4, 1, 5]) == [0, 3, 4, 8, 9, 14]


def test_range_full():
    p = ex.build_prefix([3, 1, 4, 1, 5])
    assert ex.range_sum(p, 0, 5) == 14


def test_range_middle():
    p = ex.build_prefix([3, 1, 4, 1, 5])
    assert ex.range_sum(p, 1, 4) == 1 + 4 + 1


def test_range_single():
    p = ex.build_prefix([3, 1, 4, 1, 5])
    assert ex.range_sum(p, 2, 3) == 4


def test_range_empty():
    p = ex.build_prefix([3, 1, 4])
    assert ex.range_sum(p, 1, 1) == 0


def test_negatives():
    p = ex.build_prefix([-1, 2, -3, 4])
    assert ex.range_sum(p, 0, 4) == 2
    assert ex.range_sum(p, 1, 3) == -1
