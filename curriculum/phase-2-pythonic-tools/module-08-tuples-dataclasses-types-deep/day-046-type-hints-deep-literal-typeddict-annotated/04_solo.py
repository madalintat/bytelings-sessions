"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: TypedDict + Literal in one small domain

Define:

1. A TypedDict `Event` with these required keys:
   - kind: Literal["click", "view", "purchase"]
   - user_id: int
   - amount_cents: int    (must always be present; for view/click it can be 0)

2. A function `revenue(events)`:
   - `events` is a list of `Event`.
   - Return the sum of `amount_cents` across all events whose `kind`
     is "purchase".
   - Empty list returns 0.

Constraints:
- Don't import anything beyond `typing`. No third-party libs.
- The function is a one-line generator-expression sum.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Literal, TypedDict


# TODO: define Event
class Event(TypedDict):
    pass


def revenue(events: list[Event]) -> int:
    raise NotImplementedError
