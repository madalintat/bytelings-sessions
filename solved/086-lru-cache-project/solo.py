"""Rung 4: Solo implement — solved version.

memoize_lru wraps fn with an LRUCache (OrderedDict-based for simplicity).
The wrapper exposes .hits, .misses, and .cache_clear(). Only positional
args are used as cache keys (as specified).
"""
from collections import OrderedDict
from typing import Callable


def memoize_lru(fn: Callable, capacity: int) -> Callable:
    cache: OrderedDict = OrderedDict()
    hits = 0
    misses = 0

    def wrapper(*args):
        nonlocal hits, misses
        if args in cache:
            hits += 1
            cache.move_to_end(args, last=False)
            return cache[args]
        misses += 1
        result = fn(*args)
        cache[args] = result
        cache.move_to_end(args, last=False)
        if len(cache) > capacity:
            cache.popitem(last=True)
        return result

    def cache_clear():
        nonlocal hits, misses
        cache.clear()
        hits = 0
        misses = 0

    wrapper.cache_clear = cache_clear

    # Use properties via a class trick for mutable counters.
    class _Wrapper:
        def __call__(self, *args):
            return wrapper(*args)

        @property
        def hits(self):
            return hits

        @property
        def misses(self):
            return misses

        def cache_clear(self):
            cache_clear()

    return _Wrapper()
