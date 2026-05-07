"""Rung 3: Guided implement.

Topic: a higher-order `compose`

Implement `compose(*fns)`: return a single function that applies each
of `fns` in order. compose(f, g, h)(x) == h(g(f(x))).
"""
from typing import Callable


def compose(*fns: Callable) -> Callable:
    """Return a function that applies each of fns left-to-right.

    compose(f, g, h)(x) == h(g(f(x)))

    >>> add1 = lambda x: x + 1
    >>> times2 = lambda x: x * 2
    >>> str_it = str
    >>> pipeline = compose(add1, times2, str_it)
    >>> pipeline(3)         # (3 + 1) * 2 = 8 -> '8'
    '8'
    >>> compose()(5)        # no functions = identity
    5
    >>> compose(add1)(10)
    11
    """
    # TODO: a closure that loops over fns, threading the result.
    raise NotImplementedError
