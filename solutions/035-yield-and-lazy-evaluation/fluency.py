"""Rung 2: Fluency drill — fix the two generators.

Topic: yield, lazy evaluation, yield from
"""


def count_up_to(n: int):
    """Yield 1, 2, ..., n. Inclusive."""
    # TODO: this yields 0..n-1. Fix the range so it includes n.
    for i in range(n):
        yield i


def flatten(lists):
    """Yield every element of every sublist, in order.

    >>> list(flatten([[1, 2], [3], [4, 5]]))
    [1, 2, 3, 4, 5]
    """
    # TODO: replace this nested loop with a single `yield from`.
    for sub in lists:
        for x in sub:
            yield x
