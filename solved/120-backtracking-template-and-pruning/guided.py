"""Rung 3: Guided — solved version.

P-28 (memoize-recursive) pattern: define the nested helper, decorate
with @cache, write the recurrence as straight recursion.

The inner @cache creates a new cache object per call to count_paths,
so there's no cross-call leakage — no need for manual cache_clear().

Recurrence:
  count(i, j) = 0          if out-of-bounds or grid[i][j] == 1
  count(i, j) = 1          if i == rows-1 and j == cols-1
  count(i, j) = count(i+1, j) + count(i, j+1)
"""
import functools


def count_paths(grid: list[list[int]]) -> int:
    """Count paths top-left to bottom-right moving only right or down."""
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    @functools.cache
    def count(i: int, j: int) -> int:
        # Out of bounds or blocked.
        if i >= rows or j >= cols or grid[i][j] == 1:
            return 0
        # Reached the destination.
        if i == rows - 1 and j == cols - 1:
            return 1
        # Move right or down.
        return count(i + 1, j) + count(i, j + 1)

    return count(0, 0)
