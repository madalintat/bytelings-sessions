"""Rung 2: Fluency — solved version.

Four first-class-function fixes:
  1. apply: returns `fn` (the function object) instead of `fn(x)`.
     Fix: return fn(x).
  2. sort_by_length: sorted() with no key sorts alphabetically.
     Fix: sorted(words, key=len).
  3. keep_truthy: `not predicate(x)` inverts the filter. Also,
     `filter(...)` returns an iterator, not a list. Fix: use a list
     comprehension with the correct direction.
  4. double_each: `list(nums)` copies the list unchanged. Use a
     list comprehension or map: [x * 2 for x in nums].
"""
from typing import Callable


def apply(fn: Callable, x):
    """Return fn(x)."""
    return fn(x)


def sort_by_length(words: list[str]) -> list[str]:
    """Return words sorted by their length, ascending."""
    return sorted(words, key=len)


def keep_truthy(items: list, predicate: Callable) -> list:
    """Return items for which predicate(item) is truthy."""
    return [x for x in items if predicate(x)]


def double_each(nums: list[int]) -> list[int]:
    """Return a list of each number doubled."""
    return [x * 2 for x in nums]
