"""Rung 4: Solo implement.

Topic: a memoizing closure

Implement `make_memoizer()`:

- Returns a function `memo(fn)` that takes a function `fn`.
- `memo(fn)` returns a NEW function that wraps `fn` such that:
  - The first call with a given args/kwargs computes fn(...) and
    caches the result.
  - Subsequent calls with the same args/kwargs return the cache.
- All wrapped functions share NOTHING with each other (each call to
  memo(fn) gets its own cache).
- Args may be any hashable types. Kwargs are converted to a sorted
  tuple of pairs to use in the cache key.

Examples:
    memo = make_memoizer()
    slow_calls = []
    def slow(x):
        slow_calls.append(x)
        return x * 2

    fast = memo(slow)
    assert fast(5) == 10
    assert fast(5) == 10  # second call should NOT add to slow_calls
    assert slow_calls == [5]

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Callable


def make_memoizer() -> Callable:
    raise NotImplementedError
