"""Rung 2: Fluency — solved version.

The TODOs were:
  1. cents_to_dollars used `*` instead of `/`. 100 cents = 1 dollar,
     so the conversion divides by 100.
  2. is_divisible compared n / divisor == 0, which is true only when
     n itself is 0. Divisibility is `n % divisor == 0` — modulo
     returns the remainder; if it's 0, divisor divides n cleanly.
"""


def cents_to_dollars(cents: int) -> float:
    """Convert cents to dollars. 150 cents → 1.5 dollars."""
    return cents / 100


def is_divisible(n: int, divisor: int) -> bool:
    """Return True if n is exactly divisible by divisor."""
    return n % divisor == 0
