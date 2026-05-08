"""Rung 3: Guided — solved version.

Bottom-up tabulation:
- dp[0] = 0 (base case: zero coins for target 0)
- dp[t] = 1 + min(dp[t-c] for c in coins if t-c >= 0)
- Infinity sentinel avoids confusing "unreachable" with 0.
- Final answer: dp[target] unless still infinity → return -1.
"""


def min_coins_dp(coins: list[int], target: int) -> int:
    """Return the minimum number of coins to make target, or -1."""
    INF = float("inf")
    dp = [INF] * (target + 1)
    dp[0] = 0
    for t in range(1, target + 1):
        for c in coins:
            if t - c >= 0 and dp[t - c] + 1 < dp[t]:
                dp[t] = dp[t - c] + 1
    return dp[target] if dp[target] != INF else -1
