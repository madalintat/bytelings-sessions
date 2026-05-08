"""Rung 2: Fluency drill — solved version.

Bug: apply_discount returns a negative value when discount > price.
Fix: clamp the result at zero using max(0, ...).
"""


def apply_discount(price_cents: int, discount_cents: int) -> int:
    return max(0, price_cents - discount_cents)
