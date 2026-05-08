"""HIDDEN tests for rung 4 — min_coins_topdown."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_us_coins():
    actual = ex.min_coins_topdown([1, 5, 10, 25], 30)
    diagnose(
        actual == 2,
        f"Expected 2, got {actual!r}.",
        (lambda: actual == 3,
         "3 coins is valid but not minimal — [25, 5] gives 2."),
    )


def test_greedy_trap_1():
    actual = ex.min_coins_topdown([1, 4, 5], 8)
    diagnose(
        actual == 2,
        f"Expected 2 ([4,4]), got {actual!r}.",
        (lambda: actual == 4,
         "That's the greedy answer. Top-down DP must explore ALL coin choices."),
    )


def test_greedy_trap_2():
    actual = ex.min_coins_topdown([1, 3, 4], 6)
    diagnose(
        actual == 2,
        f"Expected 2 ([3,3]), got {actual!r}.",
        (lambda: actual == 3,
         "Greedy picks [4,1,1]=3. Top-down should find [3,3]=2."),
    )


def test_greedy_trap_3():
    actual = ex.min_coins_topdown([1, 7, 10], 14)
    diagnose(
        actual == 2,
        f"Expected 2 ([7,7]), got {actual!r}.",
        (lambda: actual == 5,
         "Greedy takes 10 then four 1s. Recursion + memo finds [7,7]=2."),
    )


def test_unreachable():
    actual = ex.min_coins_topdown([2], 3)
    diagnose(
        actual == -1,
        f"Expected -1 for unreachable target, got {actual!r}.",
        (lambda: actual is None,
         "Return -1 (the integer), not None, for unreachable targets."),
    )


def test_zero_target():
    actual = ex.min_coins_topdown([1, 5], 0)
    diagnose(
        actual == 0,
        f"Expected 0 for target=0, got {actual!r}.",
        (lambda: actual == 1,
         "The base case is min_coins(0) = 0 — zero coins needed."),
    )


def test_single_coin_exact():
    actual = ex.min_coins_topdown([5], 25)
    diagnose(
        actual == 5,
        f"Expected 5 (five 5-coins), got {actual!r}.",
    )


def test_large_target_no_recursion_limit():
    result = ex.min_coins_topdown([1, 5, 10, 25], 10_000)
    assert result > 0, "Should handle large targets without RecursionError."
