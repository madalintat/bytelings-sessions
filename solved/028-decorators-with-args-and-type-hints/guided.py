"""Rung 3: Guided — solved version.

`retry(times, on)` is a 3-layer decorator factory:
  1. `retry(times, on)` — validates `times >= 1`, returns `decorator`.
  2. `decorator(fn)` — wraps fn and returns `wrapped`.
  3. `wrapped(*args, **kwargs)` — loops up to `times` attempts, catching
     only exceptions that are instances of `on`. Resets `wrapped.attempts`
     at the start of each call. Re-raises the last exception if all fail.

Key difference from Day 27's `retry`: this one takes ARGS, so it's a
3-layer factory. Day 27's was a 2-layer (no args) decorator.

Also, `on` can be a class or a tuple of classes — this is handled naturally
by `except on:` since Python allows tuples in except clauses.
"""
import functools
from typing import Callable


def retry(times: int = 3, on: type[BaseException] = Exception) -> Callable:
    """Retry decorator factory."""
    if times < 1:
        raise ValueError(f"times must be >= 1, got {times}")

    def decorator(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            wrapped.attempts = 0
            last_exc = None
            for _ in range(times):
                try:
                    wrapped.attempts += 1
                    return fn(*args, **kwargs)
                except on as exc:
                    last_exc = exc
            raise last_exc

        wrapped.attempts = 0
        return wrapped

    return decorator
