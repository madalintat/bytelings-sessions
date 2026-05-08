"""Rung 4: Solo — solved version.

`Repeat` is an *iterable*, not an iterator. The key distinction: its
`__iter__` creates a fresh `_RepeatIterator` every time, so
`list(r); list(r)` both produce the same result. If `Repeat` were its
own iterator (i.e. also had `__next__`), the second call would yield
nothing because the internal state would be exhausted.

The inner iterator materialises the flattened sequence once using
`itertools.chain.from_iterable` applied to `times` copies of `values`,
which avoids duplicating the values list while staying lazy enough for
reasonable sizes.
"""
import itertools


class _RepeatIterator:
    def __init__(self, values, times: int) -> None:
        self._it = itertools.chain.from_iterable(
            itertools.repeat(list(values), times)
        )

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._it)


class Repeat:
    def __init__(self, values, times: int) -> None:
        self._values = list(values)
        self._times = times

    def __iter__(self):
        return _RepeatIterator(self._values, self._times)
