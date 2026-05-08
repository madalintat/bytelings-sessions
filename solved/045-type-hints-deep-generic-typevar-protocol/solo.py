"""Rung 4: Solo — solved version.

`Sized` is a structural Protocol: any object that implements
`__len__(self) -> int` satisfies it, whether or not it subclasses
`Sized`. `longest` iterates once, using `max` with a key function.
`max` on an empty sequence raises ValueError, which is what the spec
requires — no need for a separate guard.
"""
from typing import Protocol


class Sized(Protocol):
    def __len__(self) -> int: ...


def longest(items: list[Sized]) -> Sized:
    if not items:
        raise ValueError("longest requires a non-empty list")
    return max(items, key=len)
