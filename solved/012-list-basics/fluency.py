"""Rung 2: Fluency — solved version.

Four basic list bugs:
  1. head: Python is 0-indexed, so the first element is items[0] not items[1].
  2. tail: items[-2] is the second-to-last. items[-1] is always the last.
  3. append_x: `items + [x]` creates a NEW list and leaves `items` unchanged.
     The test checks that items is mutated AND that the returned object is
     the same list. Use items.append(x) — it mutates in place — then return items.
  4. replace_first: items.insert(0, value) INSERTS at index 0, shifting
     everything right (grows the list). To REPLACE, use index assignment:
     items[0] = value.
"""


def head(items: list) -> object:
    """Return the first element."""
    return items[0]


def tail(items: list) -> object:
    """Return the LAST element."""
    return items[-1]


def append_x(items: list, x) -> list:
    """Append `x` to `items` in place and return the modified list."""
    items.append(x)
    return items


def replace_first(items: list, value) -> list:
    """Replace the first element with `value` (in place) and return items."""
    items[0] = value
    return items
