"""Rung 3: Guided implement.

Topic: a generic function

Implement `last_or(items, default)`:
- If `items` is non-empty, return its last element.
- If `items` is empty, return `default`.

Type the signature so:
    - `items` is `list[T]`
    - `default` is `T`
    - the return type is `T`

That is, both the list elements and the default share a single type `T`.
"""
from typing import TypeVar


T = TypeVar("T")


def last_or(items: list[T], default: T) -> T:
    """Return the last item of `items`, or `default` if empty.

    >>> last_or([1, 2, 3], 0)
    3
    >>> last_or([], "fallback")
    'fallback'
    """
    # TODO: one or two lines.
    raise NotImplementedError
