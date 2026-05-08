"""Rung 2: Fluency — solved version.

Three decorator-with-args fixes:
  1. repeat(times): the starter uses only 2 layers instead of 3. A
     decorator FACTORY needs: outer(times) -> decorator(fn) -> wrapped(*a, **kw).
     Also `@functools.wraps(times)` in the starter passes the INT `times`
     to wraps, which is wrong — wraps takes the wrapped FUNCTION.
     Fix: 3-layer structure; @functools.wraps(fn) inside wrapped.
  2. tag(label): missing @functools.wraps and the `.label` attribute.
     Fix: add @functools.wraps(fn) to wrapped, then set wrapped.label = label
     BEFORE returning.
  3. validate_positive: checks `a < 0` (negative only), but the test
     checks that 0 raises too (0 is not POSITIVE). Fix: `a <= 0`.
"""
import functools
from typing import Callable


def repeat(times: int) -> Callable:
    """Decorator factory: call the wrapped function `times` times.

    Returns a list of all return values.
    """
    def decorator(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            return [fn(*args, **kwargs) for _ in range(times)]
        return wrapped
    return decorator


def tag(label: str) -> Callable:
    """Set wrapped.label = label so callers can read it."""
    def decorator(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            return fn(*args, **kwargs)
        wrapped.label = label
        return wrapped
    return decorator


def validate_positive(fn: Callable) -> Callable:
    """No-arg decorator: ensure all positional args are > 0."""
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        for a in args:
            if a <= 0:
                raise ValueError(f"non-positive arg: {a}")
        return fn(*args, **kwargs)
    return wrapped
