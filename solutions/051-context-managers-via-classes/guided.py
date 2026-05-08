"""Rung 3: Guided implement.

Topic: a context manager that suppresses one specific exception type

Implement `Suppress(*exc_types)` — a context manager that swallows the
listed exception types and lets others propagate.

Usage:
    with Suppress(ValueError):
        int("not a number")     # silently ignored
    print("we get here")

Hint: __exit__ returning truthy suppresses the exception.
"""


class Suppress:
    def __init__(self, *exc_types: type) -> None:
        self.exc_types = exc_types

    # TODO: __enter__ returns self
    # TODO: __exit__(self, exc_type, exc, tb)
    #   - if exc_type is None, return False (no exception)
    #   - if exc_type matches any in self.exc_types, return True (suppress)
    #   - otherwise return False (re-raise)
