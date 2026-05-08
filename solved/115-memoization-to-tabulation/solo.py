"""Rung 4: Solo — solved version.

Top-down memoized recursion using @functools.cache.

The trick: @cache requires hashable arguments.  We freeze `coins` as a
tuple and define the recursive helper INSIDE the outer function so it
captures the frozen tuple via closure.  The outer function is called once
per (coins, target) pair; the inner `_helper` is memoized by `target`
only (coins is fixed per call to the outer function).

For large targets this avoids Python's default recursion limit by using
sys.setrecursionlimit or by switching to iterative.  We use
functools.lru_cache on the inner helper; large inputs will still hit the
limit — bottom-up (rung 3) is safer there.
"""
import functools


def min_coins_topdown(coins: list[int], target: int) -> int:
    """Return the minimum number of coins to make target, or -1."""
    _coins = tuple(sorted(coins))

    @functools.cache
    def _helper(remaining: int) -> float:
        if remaining == 0:
            return 0
        best = float("inf")
        for c in _coins:
            if remaining - c >= 0:
                sub = _helper(remaining - c)
                if sub + 1 < best:
                    best = sub + 1
        return best

    result = _helper(target)
    return result if result != float("inf") else -1
