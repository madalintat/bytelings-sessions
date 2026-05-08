"""Rung 3: Guided — solved version.

The recurrence: at each step, choose either to USE coin i (stay at
i, reduce amount) or SKIP it (advance to i+1, same amount). The
"stay at i" option is what allows reusing the same coin multiple
times.

Tuple coercion before the helper is the standard `@cache` fix for
unhashable list arguments. The helper itself only takes hashable
args (i + amount), so it caches cleanly.

Base cases: amount == 0 means we found a way (one). amount < 0 or
ran out of coin types means no way.
"""
from functools import cache


def count_ways(coins: list[int], amount: int) -> int:
    coins_t = tuple(coins)

    @cache
    def helper(i: int, remaining: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0 or i == len(coins_t):
            return 0
        # use coin i (stay) + skip coin i (advance)
        return helper(i, remaining - coins_t[i]) + helper(i + 1, remaining)

    return helper(0, amount)
