"""Rung 3: Guided implement — solved version.

The body is one line: n is even iff n % 2 == 0. The modulo operator
returns the remainder of integer division; for any integer n,
`n % 2` is 0 (even) or 1 (odd). Works for negatives too because
Python's `%` returns a non-negative result for a positive divisor:
-4 % 2 == 0, -7 % 2 == 1.
"""


def is_even(n: int) -> bool:
    """Return True if `n` is even, False otherwise.

    >>> is_even(2)
    True
    >>> is_even(7)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    """
    return n % 2 == 0
