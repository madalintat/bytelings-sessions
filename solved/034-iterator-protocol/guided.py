"""Rung 3: Guided — solved version.

`Squares` is a stateful iterator: `__iter__` returns `self` (so the
object works directly in `for` loops), and `__next__` returns the next
square and advances the counter, or raises `StopIteration` when
exhausted.
"""


class Squares:
    """Iterate over the first `n` squares.

    >>> list(Squares(4))
    [0, 1, 4, 9]
    >>> list(Squares(0))
    []
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.i >= self.n:
            raise StopIteration
        value = self.i ** 2
        self.i += 1
        return value
