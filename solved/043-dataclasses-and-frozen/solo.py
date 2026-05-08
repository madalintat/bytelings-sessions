"""Rung 4: Solo — solved version.

`Item` is frozen (immutable, hashable) — a value object that can be
placed in sets or used as a dict key. `Order` is mutable and uses
`field(default_factory=list)` so each order starts with its own empty
items list. `total` sums the `price_cents` of all items with a
generator expression.
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Item:
    name: str
    price_cents: int


@dataclass
class Order:
    id: int
    items: list[Item] = field(default_factory=list)


def total(order: Order) -> int:
    return sum(item.price_cents for item in order.items)
