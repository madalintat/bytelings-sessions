"""Rung 2 — fix the silent mutation.

Topic: identity, mutation, defensive copies
"""


def append_safely(lst: list, item) -> list:
    """Return a NEW list with item appended; do not mutate the input."""
    # TODO: this mutates the caller's list. Fix.
    lst.append(item)
    return lst
