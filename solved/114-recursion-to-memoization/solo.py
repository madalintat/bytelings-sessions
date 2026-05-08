"""Rung 4: Solo — solved version.

Different problem from guided's count-ways: now we want the FEWEST
coins, not the count of distinct combinations. The recurrence:

    min_coins(amount) = 1 + min(min_coins(amount - c) for c in coins
                                 if c <= amount)

Base case: amount == 0 returns 0 (zero coins needed). For
unreachable amounts, the helper returns math.inf so it doesn't
pollute the min.

Final wrap: at the top level, if the helper returned inf, the
problem is impossible — return -1 per the spec.

Patterns: P-28 (memoize-recursive).
"""
import math
from functools import cache


def min_coins(coins: list[int], amount: int) -> int:
    coins_t = tuple(coins)

    @cache
    def helper(remaining: int) -> int | float:
        if remaining == 0:
            return 0
        if remaining < 0:
            return math.inf
        best = math.inf
        for c in coins_t:
            if c <= remaining:
                best = min(best, 1 + helper(remaining - c))
        return best

    result = helper(amount)
    return -1 if result == math.inf else result
