"""Rung 2: Fluency drill — solved version.

Apply the 0/1 knapsack recurrence row by row:
  dp[i][w] = dp[i-1][w]                           # skip
  dp[i][w] = max(dp[i][w], dp[i-1][w-wi] + vi)   # take if wi <= w

Work on a deep copy so the PARTIAL constant is not mutated.
"""

ITEMS = [(1, 1), (3, 4), (4, 5), (5, 7)]
CAPACITY = 7

PARTIAL = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


def fill_table(partial: list[list[int]]) -> list[list[int]]:
    """Fill missing cells and return the complete DP table."""
    dp = [row[:] for row in partial]  # deep copy
    n = len(ITEMS)
    W = CAPACITY
    for i in range(1, n + 1):
        wi, vi = ITEMS[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if wi <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)
    return dp
