"""Rung 2: Fluency drill — switch list comps to generator expressions.

Topic: generator expressions

The two functions below build a full list and then aggregate it. Replace
each list comprehension with a generator expression so memory stays flat.
"""


def sum_of_squares(n: int) -> int:
    """Return 0 + 1 + 4 + 9 + ... + (n-1)**2."""
    # TODO: drop the [ ] so this streams instead of allocating
    return sum([i * i for i in range(n)])


def any_negative(values: list[float]) -> bool:
    """Return True if any value is < 0."""
    # TODO: same idea — replace the list comp with a generator
    return any([v < 0 for v in values])
