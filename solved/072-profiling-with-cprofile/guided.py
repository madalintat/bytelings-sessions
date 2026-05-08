"""Rung 3: Guided implement — solved version.

Profiler context manager: __enter__ creates and enables a cProfile.Profile;
__exit__ disables it and builds a pstats.Stats. top_n formats sorted output
into a string; total_time sums the tottime field from the .stats dict.
"""
import cProfile
import io
import pstats


class Profiler:
    """A small profiler context manager."""

    def __init__(self) -> None:
        self._pr: cProfile.Profile | None = None
        self._stats: pstats.Stats | None = None

    def __enter__(self) -> "Profiler":
        self._pr = cProfile.Profile()
        self._pr.enable()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self._pr.disable()
        self._stats = pstats.Stats(self._pr)

    def top_n(self, n: int = 10) -> str:
        """Return a string of the top-n entries sorted by cumulative time."""
        buf = io.StringIO()
        pstats.Stats(self._pr, stream=buf).sort_stats("cumulative").print_stats(n)
        return buf.getvalue()

    def total_time(self) -> float:
        """Sum of `tottime` across all profiled functions."""
        # stats dict values: (cc, nc, tottime, cumtime, callers)
        return sum(v[2] for v in self._stats.stats.values())
