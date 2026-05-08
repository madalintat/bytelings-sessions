"""Rung 2: Fluency — solved version.

Two decorator fixes and one working skeleton:
  1. log_calls: missing `functools.wraps`; the wrapper doesn't create
     a `.calls` list attribute; the body returns `fn` instead of calling
     it and returning the result.
     Fix: add `@functools.wraps(fn)` to `wrapped`, set `wrapped.calls = []`
     AFTER defining `wrapped` (or before returning), append (args, kwargs)
     at the start of each call, and return `fn(*args, **kwargs)`.
  2. time_calls: the wrapper is structurally fine (has @functools.wraps),
     but it's missing the `.times` attribute and the timing code.
     Fix: set `wrapped.times = []`, record start/end with
     `time.perf_counter()`, and append the elapsed float.
"""
import functools
import time


def log_calls(fn):
    """Return a wrapped version of fn that records calls in `wrapper.calls`."""
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        wrapped.calls.append((args, kwargs))
        return fn(*args, **kwargs)
    wrapped.calls = []
    return wrapped


def time_calls(fn):
    """Return a wrapper that records elapsed time per call in `wrapper.times`."""
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        wrapped.times.append(time.perf_counter() - t0)
        return result
    wrapped.times = []
    return wrapped


@log_calls
def add(a, b):
    """Sum two numbers."""
    return a + b
