"""Rung 2: Fluency drill — fix the @contextmanager.

Topic: contextlib.contextmanager

`scoped` should be a context manager that:
    - on entry, appends "enter" to the events list
    - yields the events list (so `as` exposes it)
    - on exit, appends "exit" — even if the body raised

Add the @contextmanager decorator AND wrap the yield in try/finally.
"""
from contextlib import contextmanager


# TODO: add the @contextmanager decorator above this function.
def scoped(events: list[str]):
    events.append("enter")
    yield events
    # TODO: this won't run if the body raises. Wrap the yield in
    #       try/finally so the cleanup runs no matter what.
    events.append("exit")
