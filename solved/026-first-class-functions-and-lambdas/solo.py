"""Rung 4: Solo — solved version.

`pipeline(steps)` returns a `run(value)` closure that:
  1. Applies each (name, fn) step in order, accumulating the value.
  2. Records each step's result in a trace list.
  3. Returns (final_value, trace).

The trace is built fresh on each `run()` call (it's a local variable
inside `run`, not shared), so calling `run()` twice produces independent
traces.
"""
from typing import Callable


def pipeline(steps: list[tuple[str, Callable]]) -> Callable:
    def run(value):
        trace = []
        for name, fn in steps:
            value = fn(value)
            trace.append((name, value))
        return value, trace
    return run
