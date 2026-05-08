"""Rung 3: Guided implement.

Topic: a `cache` decorator (toy version of functools.lru_cache)

Implement `cache(fn)`: wrap fn so that calls with the same args+kwargs
return cached results. Reset by deleting `wrapped.cache` (a dict).
"""
import functools


def cache(fn):
    """Memoize fn by argument tuple.

    The wrapped function exposes a `cache` dict attribute mapping
    (args_tuple, kwargs_frozenset) -> result.

    >>> calls = []
    >>> @cache
    ... def double(x):
    ...     calls.append(x)
    ...     return x * 2
    >>> double(3)
    6
    >>> double(3)
    6
    >>> calls
    [3]
    >>> double.cache[((3,), frozenset())]
    6
    """
    # TODO: closure over a dict; functools.wraps; build a hashable key
    #       from args + frozenset(kwargs.items())
    raise NotImplementedError
