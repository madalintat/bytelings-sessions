"""Tests for rung 3."""
import importlib.util
import math
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    out = ex.fractional_knapsack([(10, 60), (20, 100), (30, 120)], 50)
    assert math.isclose(out, 240.0)


def test_empty():
    assert ex.fractional_knapsack([], 10) == 0.0


def test_zero_capacity():
    assert ex.fractional_knapsack([(10, 100)], 0) == 0.0


def test_partial_first_item():
    assert math.isclose(ex.fractional_knapsack([(10, 100)], 5), 50.0)


def test_all_fit():
    assert math.isclose(ex.fractional_knapsack([(2, 10), (3, 15)], 100), 25.0)


def test_picks_higher_ratio_first():
    # Item A: value 10/weight 5 → ratio 2.0
    # Item B: value 30/weight 10 → ratio 3.0  (better)
    # Capacity 8. Should take all of B (10 wt? no, only 8 cap).
    # We can only take 8/10 of B → value 24.
    out = ex.fractional_knapsack([(5, 10), (10, 30)], 8)
    assert math.isclose(out, 24.0)
