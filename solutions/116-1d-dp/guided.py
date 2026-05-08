"""Rung 3: Guided — 0/1 knapsack, 2-D DP.

Topic: classic 0/1 knapsack with a 2-D table.

Given a list of (weight, value) items and a knapsack capacity, return
the maximum total value achievable without exceeding the capacity.
Each item can be taken at most once (the "0/1" part).

>>> knapsack_2d([(1, 1), (3, 4), (4, 5), (5, 7)], 7)
9
>>> knapsack_2d([], 10)
0
>>> knapsack_2d([(5, 10)], 4)
0
>>> knapsack_2d([(2, 3), (3, 4)], 5)
7

Recurrence (given in the README):
    dp[0][w] = 0  for all w          (no items → value 0)
    dp[i][w] = dp[i-1][w]            (skip item i)
    dp[i][w] = max(dp[i][w],
                   dp[i-1][w - wi] + vi)  if wi <= w   (take item i)

Build a 2-D list:
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

Return dp[n][capacity].
"""


def knapsack_2d(items: list[tuple[int, int]], capacity: int) -> int:
    """Return max value fitting within capacity, 0/1 knapsack.

    items: list of (weight, value) tuples.
    Uses a 2-D dp table (n+1) x (capacity+1).
    """
    raise NotImplementedError
