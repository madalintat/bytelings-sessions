"""Tests for rung 2 — greedy vs DP recognition.

Each test checks one coin-change scenario.  The `diagnose` helper
provides a teaching message when the learner gets the prediction wrong.
"""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


# ---------------------------------------------------------------------------
# Helpers (not exported — test-internal only)
# ---------------------------------------------------------------------------

def _greedy_count(coins: list[int], target: int) -> int:
    """Greedy: repeatedly subtract the largest coin that fits."""
    coins_sorted = sorted(coins, reverse=True)
    remaining = target
    count = 0
    for c in coins_sorted:
        while remaining >= c:
            remaining -= c
            count += 1
    return count if remaining == 0 else -1


def _dp_count(coins: list[int], target: int) -> int:
    """Bottom-up DP: true minimum coin count."""
    INF = float("inf")
    dp = [INF] * (target + 1)
    dp[0] = 0
    for t in range(1, target + 1):
        for c in coins:
            if t - c >= 0 and dp[t - c] + 1 < dp[t]:
                dp[t] = dp[t - c] + 1
    return dp[target] if dp[target] != INF else -1


def _actual_greedy_works(coins, target):
    return _greedy_count(coins, target) == _dp_count(coins, target)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_us_coins_greedy_works():
    coins, target = [1, 5, 10, 25], 30
    expected = True  # 25+5 = 2 coins, greedy is optimal
    actual = ex.greedy_works(coins, target)
    diagnose(
        actual == expected,
        f"greedy_works({coins}, {target}) should be True — "
        "US coins are designed so greedy is always optimal.",
        (lambda: actual is False,
         "US coins satisfy the matroid property: taking the largest coin "
         "that fits always leads to the minimum total. Mark this True."),
    )


def test_coins_1_4_5_target_8_greedy_fails():
    coins, target = [1, 4, 5], 8
    expected = False  # greedy gives 5+1+1+1=4, DP gives 4+4=2
    actual = ex.greedy_works(coins, target)
    diagnose(
        actual == expected,
        f"greedy_works({coins}, {target}) should be False — "
        "greedy picks 5 then needs 3 ones (4 coins), but 4+4 = 2 coins.",
        (lambda: actual is True,
         "Greedy takes 5 first (largest ≤ 8), leaving 3. "
         "No coin ≤ 3 except 1, so three more 1s = 4 total. "
         "But [4, 4] = 2 coins. Greedy is WRONG here — return False."),
    )


def test_coins_1_3_4_target_6_greedy_fails():
    coins, target = [1, 3, 4], 6
    expected = False  # greedy gives 4+1+1=3, DP gives 3+3=2
    actual = ex.greedy_works(coins, target)
    diagnose(
        actual == expected,
        f"greedy_works({coins}, {target}) should be False — "
        "greedy picks 4+1+1 (3 coins) but 3+3 = 2 coins.",
        (lambda: actual is True,
         "Greedy takes 4 (largest ≤ 6), leaving 2 = 1+1. Total: 3 coins. "
         "Optimal is [3, 3] = 2 coins. Greedy fails — return False."),
    )


def test_standard_coins_greedy_works():
    coins, target = [1, 2, 5, 10, 20, 50], 30
    expected = True  # 20+10 = 2 coins, greedy is optimal
    actual = ex.greedy_works(coins, target)
    diagnose(
        actual == expected,
        f"greedy_works({coins}, {target}) should be True — "
        "standard denominations (each divides the next) are greedy-safe.",
        (lambda: actual is False,
         "When each coin denomination evenly divides the next larger one, "
         "greedy is always optimal. [1,2,5,10,20,50] has that property."),
    )


def test_coins_1_7_10_target_14_greedy_fails():
    coins, target = [1, 7, 10], 14
    expected = False  # greedy gives 10+1+1+1+1=5, DP gives 7+7=2
    actual = ex.greedy_works(coins, target)
    diagnose(
        actual == expected,
        f"greedy_works({coins}, {target}) should be False — "
        "greedy picks 10 then four 1s (5 coins), but 7+7 = 2 coins.",
        (lambda: actual is True,
         "Greedy takes 10 (largest ≤ 14), leaving 4 = 1+1+1+1. "
         "Total: 5 coins. Optimal is [7, 7] = 2 coins. "
         "This is the canonical example that kills greedy — return False."),
    )
