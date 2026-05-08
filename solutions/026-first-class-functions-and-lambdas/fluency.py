"""Rung 2: Fluency drill — first-class functions.

Topic: functions as values, lambda, higher-order
"""
from typing import Callable


def apply(fn: Callable, x):
    """Return fn(x)."""
    # TODO: this returns fn itself (a function), not its result on x
    return fn


def sort_by_length(words: list[str]) -> list[str]:
    """Return words sorted by their length, ascending."""
    # TODO: sorts alphabetically; use key=len
    return sorted(words)


def keep_truthy(items: list, predicate: Callable) -> list:
    """Return items for which predicate(item) is truthy."""
    # TODO: filter returns an iterator; we need a list.
    # Also: this filters by `not predicate`, the wrong direction.
    return filter(lambda x: not predicate(x), items)


def double_each(nums: list[int]) -> list[int]:
    """Return a list of each number doubled."""
    # TODO: this returns the original list — use map (or a comprehension)
    return list(nums)
