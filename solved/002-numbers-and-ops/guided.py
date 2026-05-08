"""Rung 3: Guided — solved version.

Two-line body: guard the zero-divisor case, then return the float
division. The `: float | None` return type is honored by an explicit
`None` (not 0, not -1, not the string "error").
"""


def safe_divide(a: int, b: int) -> float | None:
    """Return a / b as a float, or None if b is 0.

    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(10, 0) is None
    True
    """
    if b == 0:
        return None
    return a / b
