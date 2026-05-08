"""Rung 2: Fluency drill — memoize a slow recursion.

Topic: @functools.cache.

`climb` counts the number of ways to climb a staircase of n steps if
you can take 1 or 2 steps at a time. The recursion is correct but
EXPONENTIAL — it'll time out for n > 30. Add @cache (one line) to
fix it.
"""
# TODO: import cache from functools and decorate the function below


def climb(n: int) -> int:
    if n <= 1:
        return 1
    return climb(n - 1) + climb(n - 2)
