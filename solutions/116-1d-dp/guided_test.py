"""Tests for rung 3 — knapsack_2d."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_readme_example():
    items = [(1, 1), (3, 4), (4, 5), (5, 7)]
    actual = ex.knapsack_2d(items, 7)
    diagnose(
        actual == 9,
        f"knapsack_2d({items}, 7) should be 9, got {actual!r}.",
        (lambda: actual == 8,
         "8 is the greedy (value/weight ratio) answer. "
         "DP finds (w=3,v=4)+(w=4,v=5)=9. Are you filling the 2D table?"),
        (lambda: actual == 7,
         "7 is just item (w=5,v=7). Check that you also consider "
         "combining lighter items."),
        (lambda: actual == 0,
         "0 means no items were taken. Make sure dp[0][w]=0 base case "
         "is in place and the loop starts at i=1."),
    )


def test_empty_items():
    actual = ex.knapsack_2d([], 10)
    diagnose(
        actual == 0,
        f"knapsack_2d([], 10) should be 0, got {actual!r}.",
        (lambda: actual != 0,
         "No items means no value — return 0 for empty item list."),
    )


def test_item_too_heavy():
    actual = ex.knapsack_2d([(5, 10)], 4)
    diagnose(
        actual == 0,
        f"knapsack_2d([(5,10)], 4) should be 0 (item doesn't fit), got {actual!r}.",
        (lambda: actual == 10,
         "The item weighs 5 but capacity is 4 — it cannot be taken."),
    )


def test_take_both():
    actual = ex.knapsack_2d([(2, 3), (3, 4)], 5)
    diagnose(
        actual == 7,
        f"knapsack_2d([(2,3),(3,4)], 5) should be 7, got {actual!r}.",
        (lambda: actual == 4,
         "You took only (w=3,v=4). Both items fit (2+3=5) for value 7."),
    )


def test_zero_capacity():
    actual = ex.knapsack_2d([(1, 100)], 0)
    diagnose(
        actual == 0,
        f"knapsack_2d([(1,100)], 0) should be 0 (capacity zero), got {actual!r}.",
        (lambda: actual != 0,
         "Capacity 0 means nothing can be taken — return 0."),
    )


def test_single_exact_fit():
    actual = ex.knapsack_2d([(3, 5)], 3)
    diagnose(
        actual == 5,
        f"knapsack_2d([(3,5)], 3) should be 5, got {actual!r}.",
        (lambda: actual == 0,
         "Item fits exactly (weight == capacity) — it should be taken."),
    )
