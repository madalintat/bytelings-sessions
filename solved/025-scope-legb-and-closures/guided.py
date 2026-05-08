"""Rung 3: Guided — solved version.

`make_rate_limiter` uses a `calls` counter in the enclosing scope:
  - `nonlocal calls` lets the inner `try_call` function increment it.
  - Before calling `fn`, check if `calls < max_calls`. If so, call fn,
    increment, and return the result. Otherwise return '__rate_limited__'
    without calling fn.

Each call to `make_rate_limiter` creates its own `calls = 0` variable,
so independent limiters don't share state.
"""
from typing import Callable


def make_rate_limiter(max_calls: int) -> Callable:
    """Return a try_call(fn, *args, **kwargs) closure capped at `max_calls`."""
    calls = 0

    def try_call(fn, *args, **kwargs):
        nonlocal calls
        if calls >= max_calls:
            return "__rate_limited__"
        calls += 1
        return fn(*args, **kwargs)

    return try_call
