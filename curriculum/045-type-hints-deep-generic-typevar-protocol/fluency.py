"""Rung 2: Fluency drill — make Box generic.

Topic: TypeVar + Generic

`Box` should be parameterized by a single type T. Add the TypeVar and
make the class Generic[T]. Update the method signatures so put/get
talk about T.

This won't change runtime behavior — it's about declaring the contract.
The tests check that the TypeVar is wired up correctly.
"""
from typing import Generic, TypeVar


# TODO: declare a TypeVar named T
T = ...  # replace with TypeVar("T")


# TODO: add Generic[T] to the bases
class Box:
    def __init__(self, value) -> None:
        self.value = value

    def get(self):
        return self.value

    def put(self, value) -> None:
        self.value = value
