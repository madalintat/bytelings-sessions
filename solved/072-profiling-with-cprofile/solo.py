"""Rung 4: Solo implement — solved version.

Profile the function, then scan the stats dict for the entry with the
highest tottime among user-defined functions. Skip built-ins (filename
starts with "~") and entries whose funcname starts with "<" or matches
the function's own name.

`pstats.Stats(pr).stats` is the right entry point: it's a dict keyed
by (filename, lineno, funcname) → (cc, ncalls, tottime, cumtime, callers).
The raw `pr.getstats()` returns lsprof tuples of a different shape.
"""
import cProfile
import pstats
from typing import Any, Callable


def bottleneck(func: Callable, *args: Any, **kwargs: Any) -> str:
    with cProfile.Profile() as pr:
        func(*args, **kwargs)

    best_name = None
    best_tt = -1.0
    best_nc = 0

    for (filename, _lineno, funcname), (_cc, nc, tt, _ct, _callers) \
            in pstats.Stats(pr).stats.items():
        # Skip built-ins (filename "~"), angle-bracketed entries
        # (<built-in>, <listcomp>), and dunder methods like __exit__
        # leaked from the cProfile context manager.
        if filename.startswith("~") or funcname.startswith("<"):
            continue
        if funcname.startswith("__") and funcname.endswith("__"):
            continue
        if funcname == func.__name__:
            continue
        if tt > best_tt:
            best_tt = tt
            best_name = funcname
            best_nc = nc

    if best_name is None:
        return "no bottleneck"
    return f"{best_name} {best_tt:.6f}s n={best_nc}"
