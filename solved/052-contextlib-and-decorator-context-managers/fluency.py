"""Rung 2: Fluency — solved version.

Two fixes:
1. The `@contextmanager` decorator is required to turn a generator
   function into a context manager.
2. The plain `yield events` doesn't protect the cleanup if the `with`
   body raises. Wrapping in `try/finally` guarantees "exit" is appended
   regardless.
"""
from contextlib import contextmanager


@contextmanager
def scoped(events: list[str]):
    events.append("enter")
    try:
        yield events
    finally:
        events.append("exit")
