"""Rung 2: Fluency — solved version.

`TypeVar("T")` declares a type variable. Making `Box` inherit from
`Generic[T]` lets type checkers know that `put(value: T)` and
`get() -> T` talk about the *same* type parameter. Runtime behaviour
is unchanged — the generic machinery is erased at runtime.
"""
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value

    def put(self, value: T) -> None:
        self.value = value
