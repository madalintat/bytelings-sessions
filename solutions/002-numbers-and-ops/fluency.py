"""Rung 2 — fix the math.

Topic: numbers, division, modulo
"""


def cents_to_dollars(cents: int) -> float:
    """Convert cents to dollars. 150 cents → 1.5 dollars."""
    # TODO: wrong operator
    return cents * 100


def is_divisible(n: int, divisor: int) -> bool:
    """Return True if n is exactly divisible by divisor."""
    # TODO: wrong comparison
    return n / divisor == 0
