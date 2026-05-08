"""Rung 2: Fluency drill — solved version.

Strategy: run BOTH greedy and DP, compare their counts.
If they agree, greedy is optimal for this input.
"""


def greedy_works(coins: list[int], target: int) -> bool:
    """Return True if greedy gives the optimal coin count, False otherwise."""
    def _greedy(coins, target):
        coins_sorted = sorted(coins, reverse=True)
        remaining = target
        count = 0
        for c in coins_sorted:
            while remaining >= c:
                remaining -= c
                count += 1
        return count if remaining == 0 else -1

    def _dp(coins, target):
        INF = float("inf")
        dp = [INF] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            for c in coins:
                if t - c >= 0 and dp[t - c] + 1 < dp[t]:
                    dp[t] = dp[t - c] + 1
        return dp[target] if dp[target] != INF else -1

    return _greedy(coins, target) == _dp(coins, target)
