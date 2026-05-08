"""Rung 2: Fluency drill — decorators that take arguments.

Topic: 3-layer decorator pattern + light type hints
"""
import functools
from typing import Callable


def repeat(times: int) -> Callable:
    """Decorator factory: call the wrapped function `times` times.

    The wrapper returns a LIST of all return values, in call order.
    """
    # TODO: only 2 layers — need an inner `decorator` layer
    @functools.wraps(times)  # also: passing times here is wrong
    def wrapped(*args, **kwargs):
        return [times(*args, **kwargs)]
    return wrapped


def tag(label: str) -> Callable:
    """Set wrapped.label = label so callers can read it."""
    def decorator(fn: Callable) -> Callable:
        # TODO: missing functools.wraps; missing the .label assignment
        def wrapped(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapped
    return decorator


def validate_positive(fn: Callable) -> Callable:
    """No-arg decorator: ensure all positional args are > 0; raise ValueError otherwise."""
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        # TODO: this checks for >= 0 (allows zero)
        for a in args:
            if a < 0:
                raise ValueError(f"non-positive arg: {a}")
        return fn(*args, **kwargs)
    return wrapped
