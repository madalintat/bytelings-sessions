"""Rung 2: Fluency drill — decorators without sugar.

Topic: a wrapper function + functools.wraps
"""
import functools


def log_calls(fn):
    """Return a wrapped version of fn that records calls in `fn.calls`.

    Each call appends (args, kwargs) to fn.calls (a LIST attribute on
    the wrapper, not the original).
    The wrapper must use functools.wraps to preserve fn.__name__.
    """
    # TODO: missing functools.wraps; missing the calls list; not actually wrapping
    def wrapped(*args, **kwargs):
        return fn
    return wrapped


def time_calls(fn):
    """Return a wrapper that records elapsed time per call in `wrapper.times`.

    Each call appends elapsed seconds (a float) to the wrapper's
    `.times` list. Use time.perf_counter().
    """
    # TODO: not capturing time, not preserving result, no times list
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapped


@log_calls
def add(a, b):
    """Sum two numbers."""
    return a + b
