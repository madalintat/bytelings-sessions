"""Rung 3: Guided — solved version.

`frozen=True` makes `Money` immutable and gives it a `__hash__`
implementation based on all fields — so Money instances can be stored
in sets or used as dict keys. `add` constructs a new `Money` rather
than mutating anything, which is the correct pattern for value objects.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    currency: str
    cents: int


def add(a: Money, b: Money) -> Money:
    """Return a + b. Raise ValueError if currencies differ."""
    if a.currency != b.currency:
        raise ValueError(
            f"currency mismatch: {a.currency!r} vs {b.currency!r}"
        )
    return Money(currency=a.currency, cents=a.cents + b.cents)
