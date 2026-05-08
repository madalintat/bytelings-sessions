"""Rung 2: Fluency — solved version.

Three function-signature fixes:
  1. greet: make `greeting` keyword-only by adding `*` before it in the
     parameter list. Add type hints. The test checks that calling
     `greet("name", "Hi")` (positionally) raises TypeError.
  2. clamp: replace the if-ladder with `max(lo, min(x, hi))`. Add type hints.
     Both forms are correct; the one-liner is idiomatic.
  3. add_to_list: mutable default argument `[]` is evaluated ONCE at
     definition time, so all calls share the same list. The fix is a
     `None` sentinel default that creates a fresh list on each call.
"""
from __future__ import annotations


def greet(name: str, *, greeting: str = "Hello") -> str:
    """Return f'{greeting}, {name}!'"""
    return f"{greeting}, {name}!"


def clamp(x: float, lo: float, hi: float) -> float:
    """Constrain x to [lo, hi]."""
    return max(lo, min(x, hi))


def add_to_list(item, container: list | None = None) -> list:
    """Append `item` to `container` and return it."""
    if container is None:
        container = []
    container.append(item)
    return container
