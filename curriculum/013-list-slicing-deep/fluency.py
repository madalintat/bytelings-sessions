"""Rung 2: Fluency drill — list slicing.

Topic: slicing, slice assignment, slice copy
"""


def first_n(items: list, n: int) -> list:
    """Return the first `n` items as a NEW list."""
    # TODO: this returns the LAST n items
    return items[-n:]


def shallow_copy(items: list) -> list:
    """Return a shallow copy of `items` using slicing."""
    # TODO: returns the same list, not a copy
    return items


def replace_middle(items: list, replacement: list) -> list:
    """Replace items[1:3] in place with `replacement` and return items.

    Note: replacement may be longer or shorter than 2.
    """
    # TODO: this is index assignment, not slice assignment
    items[1] = replacement
    return items


def reverse_in_place(items: list) -> list:
    """Reverse `items` in place using slice assignment, then return items."""
    # TODO: returns a new list rather than mutating
    return items[::-1]
