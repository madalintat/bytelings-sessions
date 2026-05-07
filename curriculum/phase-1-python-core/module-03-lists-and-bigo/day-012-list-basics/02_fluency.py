"""Rung 2: Fluency drill — list basics.

Topic: indexing, append, len, mutation
"""


def head(items: list) -> object:
    """Return the first element."""
    # TODO: Python is 0-indexed
    return items[1]


def tail(items: list) -> object:
    """Return the LAST element. Don't use len(); use a negative index."""
    # TODO: this is the second-to-last
    return items[-2]


def append_x(items: list, x) -> list:
    """Append `x` to `items` in place and return the modified list."""
    # TODO: this returns a NEW list and leaves `items` unchanged
    return items + [x]


def replace_first(items: list, value) -> list:
    """Replace the first element with `value` (in place) and return items."""
    # TODO: this prepends instead of replacing
    items.insert(0, value)
    return items
