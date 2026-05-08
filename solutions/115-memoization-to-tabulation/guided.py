"""Rung 3: Guided — min coins, bottom-up tabulation.

Topic: DP recurrence → iterative table.

Given a list of coin denominations (positive ints) and a target
amount, return the MINIMUM number of coins that sum to target.
Each coin may be used any number of times.
Return -1 if target cannot be made.

Recurrence:
    dp[0] = 0
    dp[t] = 1 + min(dp[t - c] for c in coins if t - c >= 0)

>>> min_coins_dp([1, 5, 10, 25], 30)
2
>>> min_coins_dp([1, 4, 5], 8)
2
>>> min_coins_dp([2], 3)
-1
>>> min_coins_dp([1], 0)
0

Hints:
- Create a dp list of length target + 1, initialise everything to
  infinity (or a large sentinel like target + 1).
- Set dp[0] = 0.
- For each t from 1 to target, try every coin c: if t - c >= 0,
  dp[t] = min(dp[t], dp[t - c] + 1).
- After the loop, return dp[target] if it's not infinity, else -1.
"""


def min_coins_dp(coins: list[int], target: int) -> int:
    """Return the minimum number of coins to make target, or -1.

    Uses bottom-up tabulation (no recursion).
    """
    raise NotImplementedError
