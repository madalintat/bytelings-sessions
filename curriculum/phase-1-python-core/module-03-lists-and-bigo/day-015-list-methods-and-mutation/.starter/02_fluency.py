"""Rung 2: Fluency drill — mutation vs return.

Topic: in-place methods return None
"""


def sorted_copy(items: list) -> list:
    """Return a NEW sorted list. Don't mutate the input."""
    # TODO: .sort() returns None and mutates
    return items.sort()


def reversed_copy(items: list) -> list:
    """Return a NEW reversed list. Don't mutate the input."""
    # TODO: similar trap
    return items.reverse()


def remove_evens(items: list[int]) -> list[int]:
    """Return a NEW list with even numbers removed. Don't mutate input."""
    # TODO: mutating during iteration; switch to a comprehension
    for x in items:
        if x % 2 == 0:
            items.remove(x)
    return items
