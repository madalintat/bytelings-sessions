"""Tests for rung 2 — fill the knapsack DP table."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _reference_table():
    items = ex.ITEMS
    W = ex.CAPACITY
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wi, vi = items[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if wi <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)
    return dp


def test_final_cell():
    result = ex.fill_table(ex.PARTIAL)
    actual = result[4][7]
    diagnose(
        actual == 9,
        f"dp[4][7] should be 9 (items (3,4)+(4,5)), got {actual!r}.",
        (lambda: actual == 8,
         "8 is the greedy answer. The DP should find items (w=3,v=4) "
         "and (w=4,v=5): total weight 7, value 9."),
        (lambda: actual == 7,
         "7 is just item (w=5,v=7). Check that you consider taking "
         "item 2 (w=3) and item 3 (w=4) together."),
        (lambda: actual == 0,
         "The result is 0 — you may have forgotten to copy row 0 values "
         "and to apply the recurrence for each item."),
    )


def test_row_0_unchanged():
    result = ex.fill_table(ex.PARTIAL)
    diagnose(
        result[0] == [0] * (ex.CAPACITY + 1),
        f"Row 0 should be all zeros, got {result[0]!r}.",
        (lambda: any(x != 0 for x in result[0]),
         "Row 0 represents 'no items available' — all capacities yield 0."),
    )


def test_full_table():
    ref = _reference_table()
    result = ex.fill_table(ex.PARTIAL)
    diagnose(
        result == ref,
        f"Table doesn't match reference.\nGot:      {result}\nExpected: {ref}",
        (lambda: result[1] != ref[1],
         "Row 1 (item w=1,v=1) is wrong. "
         "After taking this item, every capacity >= 1 should have value 1."),
        (lambda: result[2] != ref[2],
         "Row 2 (item w=3,v=4) is wrong. "
         "Capacity 3..5 benefits; capacity 6+ can combine with row 1."),
    )


def test_partial_not_mutated():
    import copy
    original = copy.deepcopy(ex.PARTIAL)
    ex.fill_table(ex.PARTIAL)
    diagnose(
        ex.PARTIAL == original,
        "fill_table must not modify the `partial` argument in place.",
        (lambda: ex.PARTIAL != original,
         "Use `dp = [row[:] for row in partial]` to make a deep copy "
         "before modifying."),
    )
