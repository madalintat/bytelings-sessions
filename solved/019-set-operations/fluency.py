"""Rung 2: Fluency — solved version.

Four set-operation bugs:
  1. unique_items: `{}` is an EMPTY DICT literal, not an empty set.
     The empty set is `set()`. Once created correctly, `.add(x)` works.
     Simpler: `set(items)` directly from the list.
  2. in_both: scanning `b` as a list is O(n*m). Converting to a set first
     makes membership O(1). The canonical idiom: `set(a) & set(b)` or
     `set(a).intersection(b)`.
  3. in_a_only: `b - a` gives items in b that are NOT in a. We want `a - b`.
  4. first_repeat: O(n^2) nested loops. Use a `seen` set and return on the
     first item that is already in `seen`.
"""


def unique_items(items: list) -> set:
    """Return a set of unique items in `items`."""
    return set(items)


def in_both(a: list, b: list) -> set:
    """Return the set of items present in BOTH lists."""
    return set(a) & set(b)


def in_a_only(a: set, b: set) -> set:
    """Return items in `a` that are NOT in `b`."""
    return a - b


def first_repeat(items: list):
    """Return the first item that appears at least twice, or None."""
    seen: set = set()
    for x in items:
        if x in seen:
            return x
        seen.add(x)
    return None
