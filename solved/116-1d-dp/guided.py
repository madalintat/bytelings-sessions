"""Rung 3: Guided — solved version.

2-D knapsack DP.  Row i encodes "best value using items 1..i".
Each cell: skip (copy from row above) or take (if weight fits,
look up dp[i-1][w-wi] and add vi).

Time: O(n * capacity).  Space: O(n * capacity).
"""


def knapsack_2d(items: list[tuple[int, int]], capacity: int) -> int:
    """Return max value fitting within capacity."""
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wi, vi = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if wi <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)
    return dp[n][capacity]
