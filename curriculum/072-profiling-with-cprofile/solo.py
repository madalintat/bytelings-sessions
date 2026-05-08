"""Rung 4: Solo implement.

Topic: turn a profile into a one-line bottleneck report.

Implement `bottleneck(func, *args, **kwargs) -> str`:

  - Run func(*args, **kwargs) under cProfile.
  - Find the SINGLE function (excluding all built-ins and excluding
    `func` itself) with the highest `tottime`.
  - Return a string of the form:
        "<funcname> <tottime:.6f}s n=<ncalls>"
  - If the profile has no qualifying entries (e.g., trivial func),
    return "no bottleneck".

A "function entry" key in pstats.Stats.stats is (filename, lineno, funcname).
Filter:
  - skip filename == "~" (built-ins) — wait, cProfile uses a leading
    "~" for built-ins; check for that with the file string.
  - skip funcname starting with '<' (e.g. <built-in method ...>).
  - skip the entry whose funcname matches `func.__name__`.

Hidden tests in 04_solo_test.py.
"""
from typing import Any, Callable


def bottleneck(func: Callable, *args: Any, **kwargs: Any) -> str:
    raise NotImplementedError
