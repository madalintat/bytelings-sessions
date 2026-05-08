"""Rung 4: Solo.

Topic: minimum number of coins to make `amount`.

Given a list of coin denominations and an amount, return the minimum
number of coins needed to make exactly `amount`, or -1 if impossible.
You can use any coin any number of times.

>>> min_coins([1, 2, 5], 11)
3      # 5 + 5 + 1
>>> min_coins([2], 3)
-1
>>> min_coins([1, 2, 5], 0)
0

Hints:
- Recursive shape: min_coins(amount) = 1 + min over coins c of
                                       min_coins(amount - c)
  but only if c <= amount.
- Base cases: amount == 0 → 0. amount < 0 → math.inf (or some
  sentinel) so it doesn't pollute mins.
- Use @cache. At the top level, if the result is infinity, return -1.

Tests in 04_solo_test.py are HIDDEN.

Patterns: P-28 (memoize-recursive).
"""
from functools import cache


def min_coins(coins: list[int], amount: int) -> int:
    raise NotImplementedError
