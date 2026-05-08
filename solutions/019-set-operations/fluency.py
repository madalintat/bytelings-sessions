"""Rung 2: Fluency drill — sets.

Topic: set operations and membership
"""


def unique_items(items: list) -> set:
    """Return a set of unique items in `items`."""
    # TODO: this is the dict literal — empty set is set()
    out = {}
    for x in items:
        out.add(x)
    return out


def in_both(a: list, b: list) -> set:
    """Return the set of items present in BOTH lists."""
    # TODO: linear scan over b in a loop is O(n*m)
    out = set()
    for x in a:
        if x in b:
            out.add(x)
    return out


def in_a_only(a: set, b: set) -> set:
    """Return items in `a` that are NOT in `b`."""
    # TODO: this is the wrong direction
    return b - a


def first_repeat(items: list):
    """Return the first item that appears at least twice, or None."""
    # TODO: O(n^2) — use a 'seen' set
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return items[i]
    return None
