"""Rung 3: Guided — count paths in a grid with memoized recursion.

Topic: memoize-recursive (P-28). One canonical top-down DP template.

`count_paths(grid)` counts paths from the top-left cell (0, 0) to the
bottom-right cell (rows-1, cols-1) of a 0/1 grid. A cell with value 1
is blocked; you may only move right or down.

>>> count_paths([[0, 0, 0],
...              [0, 1, 0],
...              [0, 0, 0]])
2

Recurrence:
  count(i, j) = 0                          if grid[i][j] == 1
  count(i, j) = 1                          if i == rows-1 and j == cols-1
  count(i, j) = count(i+1, j) + count(i, j+1)   otherwise
               (skip moves that go out of bounds or into a blocked cell)

Use `@functools.cache` on a nested helper that takes (i, j) as integers.

Hints:
- Define a helper `def count(i, j)` inside `count_paths`, decorate with
  @cache (import from functools).
- Base cases: out-of-bounds → 0, blocked cell → 0, bottom-right → 1.
- Call count(0, 0) to kick off.
- The cache must be cleared between calls or you'll leak state.
  Use `count.cache_clear()` after computing the result, or use
  `@cache` on the inner function (Python creates a new cache per call).
"""
import functools


def count_paths(grid: list[list[int]]) -> int:
    raise NotImplementedError
