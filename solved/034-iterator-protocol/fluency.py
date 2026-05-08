"""Rung 2: Fluency — solved version.

Two bugs fixed:
1. `__iter__` was missing — the iterator protocol requires it to return
   `self` so the object can be used in `for` loops and `iter()` calls.
2. `__next__` never raised `StopIteration`. Without the guard, the
   counter climbs past 2 forever. We raise before incrementing so
   `self.i` never goes out of range.
"""


class Range3:
    def __init__(self) -> None:
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.i >= 3:
            raise StopIteration
        value = self.i
        self.i += 1
        return value
