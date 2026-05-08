"""Rung 2: Fluency — solved version.

Two fixes:
1. `count_up_to` used `range(n)` (exclusive upper bound). Changing to
   `range(1, n + 1)` produces 1..n inclusive.
2. `flatten` used a nested loop with `yield x`. Replacing the inner
   loop with `yield from sub` delegates to the sublist's own iterator
   and is cleaner — `yield from` is the canonical idiom for "stream
   everything from a sub-iterable".
"""


def count_up_to(n: int):
    """Yield 1, 2, ..., n. Inclusive."""
    for i in range(1, n + 1):
        yield i


def flatten(lists):
    """Yield every element of every sublist, in order.

    >>> list(flatten([[1, 2], [3], [4, 5]]))
    [1, 2, 3, 4, 5]
    """
    for sub in lists:
        yield from sub
