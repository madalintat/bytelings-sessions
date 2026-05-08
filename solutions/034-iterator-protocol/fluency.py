"""Rung 2: Fluency drill — fix the iterator protocol on this class.

Topic: __iter__ and __next__

`Range3` should yield 0, 1, 2 and then stop. It's missing one method
and the other has a tiny bug. Fix both.
"""


class Range3:
    def __init__(self) -> None:
        self.i = 0

    # TODO: add __iter__ — should return self

    def __next__(self) -> int:
        # TODO: this never raises StopIteration. Fix it.
        value = self.i
        self.i += 1
        return value
