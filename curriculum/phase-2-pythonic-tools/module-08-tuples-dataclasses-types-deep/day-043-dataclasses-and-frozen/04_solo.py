"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a small dataclass-driven domain

Define two dataclasses:

1. `Item` (frozen=True):
   - name: str
   - price_cents: int

2. `Order` (NOT frozen):
   - id: int
   - items: list[Item]   (default factory = list)

Then implement `total(order)` returning the sum of `price_cents` over
all items in the order. An order with no items has total 0.

Constraints:
- The default for `Order.items` must be a fresh list per Order.
- `Item` instances must be hashable (frozen=True does this for you).
- Don't use any external libraries.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from dataclasses import dataclass


# TODO: define Item and Order
class Item:
    pass


class Order:
    pass


def total(order: "Order") -> int:
    raise NotImplementedError
