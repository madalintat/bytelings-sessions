"""Rung 2: Fluency drill — solved version.

profile_call wraps the function call in cProfile.Profile(), redirects
pstats output to an io.StringIO, and returns (result, stats_text).
Sorting by "cumulative" shows the hot call path first.
"""
import cProfile
import io
import pstats
from typing import Any, Callable


def profile_call(func: Callable, *args: Any) -> tuple[Any, str]:
    with cProfile.Profile() as pr:
        result = func(*args)
    buf = io.StringIO()
    pstats.Stats(pr, stream=buf).sort_stats("cumulative").print_stats(10)
    return result, buf.getvalue()
