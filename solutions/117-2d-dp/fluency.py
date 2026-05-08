"""Rung 2: Fluency drill — fix the unique-paths recurrence.

Topic: 2D DP — dp[r][c] = dp[r-1][c] + dp[r][c-1].

`unique_paths` should return the number of paths from (0,0) to
(m-1,n-1) moving only right or down. The recurrence indices are
wrong — it's reading from the wrong neighbors.
"""


def unique_paths(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            # TODO: should add the cell ABOVE (dp[r-1][c]) and the cell
            # to the LEFT (dp[r][c-1]). The indices below are wrong.
            dp[r][c] = dp[r][c] + dp[r - 1][c - 1]
    return dp[m - 1][n - 1]
