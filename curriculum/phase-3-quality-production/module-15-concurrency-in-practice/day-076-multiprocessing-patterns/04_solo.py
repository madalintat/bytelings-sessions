"""Rung 4: Solo implement.

Topic: build a parallel reduce.

Implement `parallel_sum_of_squares(items, max_workers=4)`:

  - Returns sum(x * x for x in items).
  - Uses ProcessPoolExecutor for the per-item squaring.
  - The summation can happen in the main process.

This is the "map" half done in parallel, then a serial "reduce" —
a common shape when the per-item work is heavy and the combine is
cheap.

Constraints:
  - Use a top-level `_square` function as the pool worker.
  - Use ProcessPoolExecutor (NOT threads).
  - Empty list -> 0.

Hidden tests in 04_solo_test.py.
"""
from concurrent.futures import ProcessPoolExecutor


def _square(x: int) -> int:
    return x * x


def parallel_sum_of_squares(items: list[int], max_workers: int = 4) -> int:
    raise NotImplementedError
