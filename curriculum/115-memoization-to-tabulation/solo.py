"""Rung 4: Solo — min coins, top-down memoization.

Topic: same coin-change problem as rung 3, but top-down with @cache.

Hidden tests in solo_test.py — don't peek before solving.

Implement `min_coins_topdown(coins, target) -> int`.

Contract:
- Return the minimum number of coins (from `coins`) that sum to
  `target`. Each coin may be used any number of times.
- Return -1 if `target` cannot be made.

Recurrence:
    min_coins(0) = 0
    min_coins(t) = 1 + min(min_coins(t - c) for c in coins if t - c >= 0)

Use @functools.cache for memoization.  Note that `cache` only works
on hashable arguments — you'll need to freeze `coins` (e.g. pass it
as a tuple or put the inner helper inside the function).

Patterns: P-28 (memoize-recursive).
"""
import functools


def min_coins_topdown(coins: list[int], target: int) -> int:
    """Return the minimum number of coins to make target, or -1.

    Uses top-down recursion with @functools.cache.
    """
    raise NotImplementedError
