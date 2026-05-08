"""Rung 2: Fluency — solved version.

Removing the square brackets `[ ]` turns a list comprehension into a
generator expression. `sum()` and `any()` both accept any iterable, so
no list needs to be allocated. For large `n` or long value lists this
keeps memory flat — `O(1)` instead of `O(n)`.
"""


def sum_of_squares(n: int) -> int:
    """Return 0 + 1 + 4 + 9 + ... + (n-1)**2."""
    return sum(i * i for i in range(n))


def any_negative(values: list[float]) -> bool:
    """Return True if any value is < 0."""
    return any(v < 0 for v in values)
