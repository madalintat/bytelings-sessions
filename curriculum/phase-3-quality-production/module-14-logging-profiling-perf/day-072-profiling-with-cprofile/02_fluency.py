"""Rung 2: Fluency drill — implement a small profiling helper.

Topic: cProfile + pstats.

`profile_call(func, *args)` should:
  - Run `func(*args)` inside a cProfile.Profile() context.
  - Return a tuple (result, stats_text), where:
      - result    : whatever func returned
      - stats_text: a string of the top-10 entries by CUMULATIVE time,
                    captured by writing pstats output to an io.StringIO.

The tests run a function and check that:
  - the result is propagated,
  - stats_text mentions our function's name (it appears in the output).
"""
import cProfile
import io
import pstats
from typing import Any, Callable


def profile_call(func: Callable, *args: Any) -> tuple[Any, str]:
    # TODO: implement using cProfile.Profile() context, pstats.Stats,
    # and an io.StringIO sink for print_stats(10).
    raise NotImplementedError
