"""Rung 3: Guided — solved version.

`last_or` is generic over `T`: both `items: list[T]` and
`default: T` share the same type variable, so a type checker can
verify that the default has the same element type as the list.
The body is a one-liner: index -1 if the list is non-empty, else return
the default.
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
    return items[-1] if items else default
