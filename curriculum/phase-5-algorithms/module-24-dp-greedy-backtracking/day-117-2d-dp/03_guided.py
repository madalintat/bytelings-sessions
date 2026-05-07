"""Rung 3: Guided — minimum path sum on a grid.

Topic: same shape as unique_paths, but tracks min sum.

Given an m×n grid of non-negative ints, return the minimum sum along
any path from top-left to bottom-right, moving only right or down.

>>> min_path_sum([[1,3,1],[1,5,1],[4,2,1]])
7    # 1 -> 3 -> 1 -> 1 -> 1
>>> min_path_sum([[5]])
5
>>> min_path_sum([[1,2,3]])
6
>>> min_path_sum([])
0

Hints:
- dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
- Base: dp[0][0] = grid[0][0]. First row: cumulative sum across.
  First column: cumulative sum down.
- Empty grid (no rows) → 0.
"""


def min_path_sum(grid: list[list[int]]) -> int:
    raise NotImplementedError
