"""Rung 4: Solo — solved version.

1-D rolling array knapsack.

The trick: iterating `w` from `capacity` DOWN to `wi` ensures that
when we update dp[w], the value dp[w - wi] still reflects the state
BEFORE item i was considered (i.e., it's the same as dp[i-1][w-wi]
in the 2-D table).  Left-to-right would let an item be counted twice,
turning this into the unbounded knapsack.

Time: O(n * capacity).  Space: O(capacity) — only one row alive.
"""


def knapsack_1d(items: list[tuple[int, int]], capacity: int) -> int:
    """Return max value fitting within capacity using a 1-D dp array."""
    dp = [0] * (capacity + 1)
    for wi, vi in items:
        # Iterate RIGHT-TO-LEFT so each item is used at most once.
        for w in range(capacity, wi - 1, -1):
            dp[w] = max(dp[w], dp[w - wi] + vi)
    return dp[capacity]
