"""Rung 4: Solo — solved version.

`Event` is a TypedDict with a `kind` narrowed by `Literal`. `revenue`
filters by `kind == "purchase"` and sums `amount_cents` — a one-line
generator-expression `sum` as the spec specifies.
"""
from typing import Literal, TypedDict


class Event(TypedDict):
    kind: Literal["click", "view", "purchase"]
    user_id: int
    amount_cents: int


def revenue(events: list[Event]) -> int:
    return sum(e["amount_cents"] for e in events if e["kind"] == "purchase")
