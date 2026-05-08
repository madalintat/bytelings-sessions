"""Rung 3: Guided implement.

Topic: a `retry(times, on=Exception)` decorator factory

Implement `retry(times, on)`: 3-layer decorator that retries fn up to
`times` times, only catching exceptions that are instances of `on`.
"""
import functools
from typing import Callable


def retry(times: int = 3, on: type[BaseException] = Exception) -> Callable:
    """Retry decorator factory.

    Args:
        times: total number of attempts. Must be >= 1; otherwise raise
            ValueError at decoration time.
        on: an exception class (or tuple of classes) to catch.

    Returns:
        A decorator. The wrapped function:
        - returns fn(*args, **kwargs) on the first success.
        - retries up to `times` total attempts on caught exceptions.
        - re-raises the last caught exception if all attempts fail.
        - exposes wrapped.attempts: count of total attempts in the
          most recent CALL (reset to 0 at start of each call).

    >>> attempts = []
    >>> @retry(times=3)
    ... def maybe():
    ...     attempts.append(1)
    ...     if len(attempts) < 2:
    ...         raise RuntimeError("nope")
    ...     return "ok"
    >>> maybe()
    'ok'
    >>> maybe.attempts
    2
    """
    # TODO: validate `times`; build decorator -> wrapped using functools.wraps.
    raise NotImplementedError
