"""Rung 4: Solo implement.

Topic: write `memoize_lru(fn, capacity)` — a decorator-style memoizer
backed by your own LRU. Build it from scratch (no functools.lru_cache).

Spec:
    `memoize_lru(fn, capacity)` returns a callable that:
      - When called with positional arguments, looks up (args) in an
        internal LRU cache.
      - On hit: returns cached value, marks key as most-recently-used.
      - On miss: calls fn(*args), stores result, returns it.
      - When the cache is full and a new key is inserted, evicts LRU.

    The wrapped callable must expose:
      - .hits: int    — count of cache hits
      - .misses: int  — count of cache misses
      - .cache_clear() -> None  — empty the cache and zero counters

    Only positional args; we ignore kwargs in this exercise.

Example:
    calls = []
    def slow(n):
        calls.append(n)
        return n * 2
    f = memoize_lru(slow, capacity=2)
    f(1); f(2); f(1)
    assert calls == [1, 2]            # second f(1) was cached
    assert f.hits == 1 and f.misses == 2

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Callable


def memoize_lru(fn: Callable, capacity: int) -> Callable:
    raise NotImplementedError
