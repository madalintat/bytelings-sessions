"""HIDDEN tests for rung 4 — knapsack_1d."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_readme_example():
    actual = ex.knapsack_1d([(1, 1), (3, 4), (4, 5), (5, 7)], 7)
    diagnose(
        actual == 9,
        f"Expected 9, got {actual!r}.",
        (lambda: actual == 8,
         "8 is the greedy answer. 1-D DP must explore all combinations."),
        (lambda: actual == 12,
         "12 would mean double-counting. Remember to iterate capacity "
         "in REVERSE (right-to-left) to avoid reusing items."),
    )


def test_empty():
    actual = ex.knapsack_1d([], 10)
    diagnose(
        actual == 0,
        f"Expected 0 for empty items, got {actual!r}.",
        (lambda: actual != 0,
         "No items means no value — dp starts all-zeros."),
    )


def test_item_too_heavy():
    actual = ex.knapsack_1d([(5, 10)], 4)
    diagnose(
        actual == 0,
        f"Expected 0 (item too heavy), got {actual!r}.",
        (lambda: actual == 10,
         "Item weight 5 exceeds capacity 4 — it cannot be taken."),
    )


def test_take_both():
    actual = ex.knapsack_1d([(2, 3), (3, 4)], 5)
    diagnose(
        actual == 7,
        f"Expected 7, got {actual!r}.",
        (lambda: actual == 4,
         "Only one item was taken. Both fit (2+3=5); iterate in reverse "
         "so each item is used at most once."),
    )


def test_no_double_counting():
    """Forward iteration would give dp[4] = 8 (uses item (2,4) twice)."""
    actual = ex.knapsack_1d([(2, 4)], 4)
    diagnose(
        actual == 4,
        f"Expected 4 (one item, 0/1 constraint), got {actual!r}.",
        (lambda: actual == 8,
         "You got 8, which means the (w=2,v=4) item was used twice. "
         "This is the 0/1 knapsack — each item once. "
         "Iterate w from capacity DOWN to wi."),
    )


def test_zero_capacity():
    actual = ex.knapsack_1d([(1, 100)], 0)
    diagnose(
        actual == 0,
        f"Expected 0, got {actual!r}.",
    )


def test_single_exact():
    actual = ex.knapsack_1d([(3, 5)], 3)
    diagnose(
        actual == 5,
        f"Expected 5, got {actual!r}.",
        (lambda: actual == 0,
         "Item weight equals capacity — it should be taken."),
    )


def test_matches_2d():
    """1-D and 2-D must agree on several inputs."""
    def knapsack_2d_ref(items, cap):
        n = len(items)
        dp = [[0] * (cap + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            wi, vi = items[i - 1]
            for w in range(cap + 1):
                dp[i][w] = dp[i - 1][w]
                if wi <= w:
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)
        return dp[n][cap]

    cases = [
        ([(2, 6), (2, 10), (3, 12)], 5),
        ([(1, 1), (2, 6), (3, 10), (5, 16)], 7),
        ([(4, 40), (3, 30), (2, 20)], 6),
    ]
    for items, cap in cases:
        expected = knapsack_2d_ref(items, cap)
        actual = ex.knapsack_1d(items, cap)
        assert actual == expected, (
            f"knapsack_1d({items}, {cap}) = {actual}, "
            f"expected {expected} (from 2D reference)."
        )
