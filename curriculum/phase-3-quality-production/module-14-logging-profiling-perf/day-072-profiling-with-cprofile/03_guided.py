"""Rung 3: Guided implement — a profiler context manager.

Topic: writing a reusable `with profiler(): ...` block.

Real-world framing: in production you'll wrap suspect code in a
profiler block, dump stats to a file, then walk away. Here we build
a small version that captures stats into an attribute you can inspect.
"""
import cProfile
import io
import pstats


class Profiler:
    """A small profiler context manager.

    Usage:
        with Profiler() as p:
            do_work()
        print(p.top_n(5))         # top 5 lines by cumtime
        print(p.total_time())     # sum of all tottime
    """

    def __init__(self) -> None:
        self._pr: cProfile.Profile | None = None
        self._stats: pstats.Stats | None = None

    def __enter__(self) -> "Profiler":
        # TODO: create a cProfile.Profile, enable() it, store on self._pr.
        raise NotImplementedError

    def __exit__(self, exc_type, exc, tb) -> None:
        # TODO: disable() the profile, build pstats.Stats from it,
        # store on self._stats. Do NOT swallow exceptions (return None / falsy).
        raise NotImplementedError

    def top_n(self, n: int = 10) -> str:
        """Return a string of the top-n entries sorted by cumulative time."""
        # TODO: write pstats output (sorted by 'cumulative') to an
        # io.StringIO and return the string.
        raise NotImplementedError

    def total_time(self) -> float:
        """Sum of `tottime` across all profiled functions."""
        # TODO: pstats.Stats has a `.stats` dict where each value is a
        # tuple (cc, nc, tt, ct, callers). Sum the `tt` (tottime) field.
        raise NotImplementedError
