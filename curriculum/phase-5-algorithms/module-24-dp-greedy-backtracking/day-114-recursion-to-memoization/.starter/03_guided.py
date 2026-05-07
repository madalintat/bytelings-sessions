"""Rung 3: Guided — memoized coin change (counting ways).

Topic: classic counting DP via recursion + @cache.

Given a list of distinct positive coin denominations and a target
amount, return the number of distinct ways to make `amount` using
any number of each coin. (Same multiset = same way; order doesn't
matter.)

>>> count_ways([1, 2, 5], 5)
4   # 5; 2+2+1; 2+1+1+1; 1+1+1+1+1
>>> count_ways([2], 3)
0
>>> count_ways([1, 2, 5], 0)
1   # one way: use no coins

Hints:
- The recursion: count_ways(coins, amount) thinks "for the i-th coin,
  either skip it (use coins[i+1:]) or use one and stay on the same
  index". Use a helper that takes (i, amount).
- Base cases: amount == 0 → 1 way. amount < 0 or i == len(coins) → 0.
- Decorate the helper with @cache. Tuples are hashable; lists aren't.
"""
from functools import cache


def count_ways(coins: list[int], amount: int) -> int:
    raise NotImplementedError
