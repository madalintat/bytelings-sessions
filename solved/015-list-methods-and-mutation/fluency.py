"""Rung 2: Fluency — solved version.

Three mutation traps:
  1. sorted_copy: list.sort() sorts in place and RETURNS NONE. Use the
     built-in `sorted(items)` which returns a new sorted list.
  2. reversed_copy: list.reverse() returns None too. Use `list(reversed(items))`
     or `items[::-1]` — both return a new list.
  3. remove_evens: mutating a list while iterating over it skips elements
     (because removing shifts indices). The idiomatic fix is a list
     comprehension that builds a NEW list: [x for x in items if x % 2 != 0].
"""


def sorted_copy(items: list) -> list:
    """Return a NEW sorted list. Don't mutate the input."""
    return sorted(items)


def reversed_copy(items: list) -> list:
    """Return a NEW reversed list. Don't mutate the input."""
    return items[::-1]


def remove_evens(items: list[int]) -> list[int]:
    """Return a NEW list with even numbers removed. Don't mutate input."""
    return [x for x in items if x % 2 != 0]
