"""Rung 3: Guided implement.

Topic: frozen dataclass as a hashable value object

Define a frozen dataclass `Money` with two fields:
    currency: str    # e.g. "USD"
    cents:    int    # whole cents, no floats!

Then implement `add(a, b)`:
- If `a.currency != b.currency`, raise ValueError.
- Otherwise return a new `Money` with the same currency and the sum
  of the cents.

Frozen dataclasses are hashable, so the tests will use a set of them.
"""
from dataclasses import dataclass


# TODO: declare Money as a frozen dataclass.
@dataclass
class Money:
    currency: str
    cents: int


def add(a: Money, b: Money) -> Money:
    """Return a + b. Raise ValueError if currencies differ."""
    # TODO: check currencies, build a new Money.
    raise NotImplementedError
