"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: estimate elapsed time for concurrent workloads

Implement `elapsed_seconds(durations, concurrent)`:

- `durations` is a list of non-negative floats representing how long
  each task takes on its own.
- If `concurrent` is False, the tasks run sequentially. Total elapsed
  time is the sum of all durations.
- If `concurrent` is True, all tasks run at the same time on a single
  event loop. Total elapsed time is the maximum of all durations.
- An empty list returns 0.0.

This is the back-of-envelope math you'll do for the rest of the module.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def elapsed_seconds(durations: list[float], concurrent: bool) -> float:
    raise NotImplementedError
