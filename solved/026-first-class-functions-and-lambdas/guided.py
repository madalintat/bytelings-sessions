"""Rung 3: Guided — solved version.

`compose(*fns)` returns a closure that threads a value through all
functions left-to-right: compose(f, g, h)(x) == h(g(f(x))).

Implementation: use `functools.reduce` with a lambda that applies the
accumulator to each function, or an explicit loop.

The explicit loop is clearer for learners:
    def composed(x):
        for fn in fns:
            x = fn(x)
        return x

`compose()` with no functions is the identity: the loop doesn't run,
and the initial value is returned unchanged.
"""
from typing import Callable


def compose(*fns: Callable) -> Callable:
    """Return a function that applies each of fns left-to-right.

    >>> add1 = lambda x: x + 1
    >>> times2 = lambda x: x * 2
    >>> compose(add1, times2)(3)
    8
    >>> compose()(5)
    5
    """
    def composed(x):
        for fn in fns:
            x = fn(x)
        return x
    return composed
