"""Rung 3: Guided — solved version.

power(a, b) = a * power(a, b-1), base case power(a, 0) = 1.
The recursion unwinds b levels deep, then bubbles back up multiplying
by a each time. No built-in ** operator is used.
"""


def power(a: int, b: int) -> int:
    """Return a ** b for non-negative integer b, recursively.

    >>> power(2, 0)
    1
    >>> power(3, 4)
    81
    >>> power(7, 1)
    7
    """
    if b == 0:
        return 1
    return a * power(a, b - 1)
