"""Rung 3: Guided implement.

Topic: a "rate limiter"-style closure

Implement `make_rate_limiter(max_calls)`:
- Returns a function `try_call(fn, *args, **kwargs)`.
- If at most `max_calls` have been made through this limiter so far,
  call fn(*args, **kwargs), increment the count, and return its result.
- Otherwise return the special string '__rate_limited__' WITHOUT
  calling fn (so we don't side-effect).
"""
from typing import Callable


def make_rate_limiter(max_calls: int) -> Callable:
    """Return a try_call(fn, *args, **kwargs) closure capped at `max_calls`.

    >>> rl = make_rate_limiter(2)
    >>> rl(lambda: 'ok')
    'ok'
    >>> rl(lambda: 'ok')
    'ok'
    >>> rl(lambda: 'ok')
    '__rate_limited__'

    Independent limiters don't share state.
    """
    # TODO: 4-6 lines using nonlocal.
    raise NotImplementedError
