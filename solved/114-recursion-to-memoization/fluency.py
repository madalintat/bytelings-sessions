"""Rung 2: Fluency — solved version.

`@functools.cache` is the entire fix. It memoizes the function: each
unique argument value computes once, every subsequent call with the
same argument hits the cache. The exponential `climb(40)` collapses
to linear.

The decorator IS the algorithmic improvement. Same recurrence, same
function body, vastly different complexity.
"""
from functools import cache


@cache
def climb(n: int) -> int:
    if n <= 1:
        return 1
    return climb(n - 1) + climb(n - 2)
