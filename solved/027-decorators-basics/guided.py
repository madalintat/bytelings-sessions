"""Rung 3: Guided — solved version.

`cache` is a simple memoizing decorator (no TTL, no max size):
  1. Define `store = {}` in the closure to hold the cache.
  2. Build a hashable key: `(args, frozenset(kwargs.items()))`.
  3. If the key is in `store`, return the cached result.
  4. Otherwise call `fn`, store the result, and return it.
  5. Expose `wrapped.cache = store` so tests can inspect it.
  6. `@functools.wraps(fn)` preserves `__name__` and `__doc__`.

This is essentially `functools.lru_cache(maxsize=None)` implemented
by hand. Knowing the implementation helps you understand why
`lru_cache` requires hashable arguments.
"""
import functools


def cache(fn):
    """Memoize fn by argument tuple."""
    store: dict = {}

    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in store:
            store[key] = fn(*args, **kwargs)
        return store[key]

    wrapped.cache = store
    return wrapped
