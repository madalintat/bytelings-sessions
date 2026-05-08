"""Tests for rung 3 — min_coins_dp (bottom-up tabulation)."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_us_coins_30():
    actual = ex.min_coins_dp([1, 5, 10, 25], 30)
    diagnose(
        actual == 2,
        f"min_coins_dp([1,5,10,25], 30) should be 2 (25+5), got {actual!r}.",
        (lambda: actual == 3,
         "3 coins is not optimal — [25, 5] hits 30 in 2 coins."),
        (lambda: actual == 6,
         "You may be adding 1+5+24 coins. Check that dp[0]=0 is your base."),
    )


def test_greedy_trap():
    actual = ex.min_coins_dp([1, 4, 5], 8)
    diagnose(
        actual == 2,
        f"min_coins_dp([1,4,5], 8) should be 2 ([4,4]), got {actual!r}.",
        (lambda: actual == 4,
         "4 is the greedy answer ([5,1,1,1]) not the DP answer. "
         "Your table must consider ALL coins at each step, not just the largest."),
        (lambda: actual == 3,
         "3 coins isn't reachable for target=8 with [1,4,5]. "
         "Check the dp update loop — you may have an off-by-one."),
    )


def test_second_greedy_trap():
    actual = ex.min_coins_dp([1, 3, 4], 6)
    diagnose(
        actual == 2,
        f"min_coins_dp([1,3,4], 6) should be 2 ([3,3]), got {actual!r}.",
        (lambda: actual == 3,
         "3 is the greedy answer ([4,1,1]). DP should find [3,3]=2. "
         "Make sure you loop over every coin c, not just the largest."),
    )


def test_exact_coin():
    actual = ex.min_coins_dp([1, 4, 5], 4)
    diagnose(
        actual == 1,
        f"min_coins_dp([1,4,5], 4) should be 1, got {actual!r}.",
        (lambda: actual == 4,
         "Four 1-coins also sum to 4, but one 4-coin is fewer. "
         "The recurrence minimises — check the min() direction."),
    )


def test_unreachable():
    actual = ex.min_coins_dp([2], 3)
    diagnose(
        actual == -1,
        f"min_coins_dp([2], 3) should be -1 (unreachable), got {actual!r}.",
        (lambda: actual == 2,
         "You can't make 3 with only 2-coins (3 is odd). Return -1."),
    )


def test_zero_target():
    actual = ex.min_coins_dp([1, 5], 0)
    diagnose(
        actual == 0,
        f"min_coins_dp([1,5], 0) should be 0 (empty selection), got {actual!r}.",
        (lambda: actual == 1,
         "Target 0 requires zero coins — dp[0] should be 0 as the base case."),
    )
