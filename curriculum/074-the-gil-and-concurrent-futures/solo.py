"""Rung 4: Solo implement.

Topic: parallel map with bounded concurrency and progress reporting.

Implement `parallel_apply(items, fn, max_workers=8) -> list`:

  - Apply `fn` to each item in parallel using ThreadPoolExecutor.
  - Return results IN INPUT ORDER (like map, not as_completed).
  - If `fn(item)` raises, the corresponding result MUST be the
    Exception object itself (not raised). Result type: Any | Exception.
  - max_workers is honored (just pass it through to the executor).

Hidden tests in 04_solo_test.py.
"""
from typing import Any, Callable


def parallel_apply(
    items: list[Any],
    fn: Callable[[Any], Any],
    max_workers: int = 8,
) -> list[Any]:
    raise NotImplementedError
