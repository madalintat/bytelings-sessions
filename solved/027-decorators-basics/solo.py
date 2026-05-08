"""Rung 4: Solo — solved version.

`retry` wraps `fn` to attempt up to 3 calls before giving up.
  - On success, bump `wrapped.successes` and return the result.
  - On exception, bump `wrapped.failures` and try again.
  - After 3 failures, re-raise the last exception.

Counters are cumulative across the wrapped function's lifetime.
"""
import functools


def retry(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        last_exc = None
        for _ in range(3):
            try:
                result = fn(*args, **kwargs)
                wrapped.successes += 1
                return result
            except Exception as exc:
                last_exc = exc
                wrapped.failures += 1
        raise last_exc

    wrapped.successes = 0
    wrapped.failures = 0
    return wrapped
