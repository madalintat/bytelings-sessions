"""Rung 4: Solo — solved version.

`make_memoizer` returns a function `memo(fn)` that wraps `fn` with
its own private cache dict.

Each call to `memo(fn)` creates a new `cache = {}` in the closure,
so different wrapped functions don't share a cache.

Cache key: `(args, tuple(sorted(kwargs.items())))` — a tuple of the
positional args and a sorted-tuple of keyword pairs. This makes the key
hashable regardless of kwarg ordering.

The wrapper checks the cache before calling `fn`; if found, returns
cached result. If not, calls `fn`, stores the result, and returns it.

`functools.wraps` is not required by the tests here but is good practice.
"""
from typing import Callable


def make_memoizer() -> Callable:
    def memo(fn: Callable) -> Callable:
        cache: dict = {}

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                cache[key] = fn(*args, **kwargs)
            return cache[key]

        return wrapper

    return memo
