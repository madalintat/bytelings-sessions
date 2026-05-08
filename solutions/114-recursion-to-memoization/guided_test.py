"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.count_ways([1, 2, 5], 5) == 4


def test_no_solution():
    assert ex.count_ways([2], 3) == 0


def test_zero_amount():
    assert ex.count_ways([1, 2, 5], 0) == 1


def test_just_one_coin():
    assert ex.count_ways([3], 9) == 1


def test_larger():
    assert ex.count_ways([1, 2, 5], 11) == 11


def test_must_be_fast():
    """Without memoization this is slow. With it, it's instant."""
    assert ex.count_ways([1, 2, 5, 10, 20, 50], 100) > 0
