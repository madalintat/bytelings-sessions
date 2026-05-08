"""Rung 4: Solo — solved version.

Sequential elapsed time is the sum of all durations (each task waits
for the previous one). Concurrent elapsed time is the maximum (they
all run at the same time; we wait for the slowest). Both reduce to a
single built-in call with a sensible default for the empty case.
"""


def elapsed_seconds(durations: list[float], concurrent: bool) -> float:
    if not durations:
        return 0.0
    return max(durations) if concurrent else sum(durations)
