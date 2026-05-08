"""Rung 3: Guided implement.

Topic: write an iterator class from scratch

Implement `Squares(n)` — an iterator that yields 0**2, 1**2, ..., (n-1)**2.

The signature, docstring, and required behavior are below.
You write `__iter__` and `__next__`.
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

    # TODO: implement __iter__ (one line)
    # TODO: implement __next__
    #   - if self.i >= self.n, raise StopIteration
    #   - otherwise return self.i ** 2 and advance self.i
