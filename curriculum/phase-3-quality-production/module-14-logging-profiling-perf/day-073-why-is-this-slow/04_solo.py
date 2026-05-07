"""Rung 4: Solo implement.

Topic: pick the right data structure.

Implement `find_pairs(xs, target) -> list[tuple[int, int]]`:

  - Returns all pairs (a, b) with a < b, both in `xs`, where a + b == target.
  - Each pair appears once, even if the inputs contain duplicates.
  - Order: ascending by `a`, ties by `b`.

The naive O(n^2) version will time out the perf test. Use a set-based
single-pass approach:
  - Iterate. For each x, check whether (target - x) is in a `seen` set.
  - If yes, that's a pair.
  - Add x to `seen`.
  - To handle duplicates and ordering, dedupe + sort the result.

Hidden tests in 04_solo_test.py.
"""


def find_pairs(xs: list[int], target: int) -> list[tuple[int, int]]:
    raise NotImplementedError
