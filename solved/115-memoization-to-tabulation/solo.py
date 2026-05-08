"""Rung 4: Solo — solved version (depth-safe).

The day's spec asks for top-down memoized recursion. The literal
@functools.cache form is the natural answer:

    @cache
    def _helper(remaining):
        if remaining == 0: return 0
        ...
        return min(1 + _helper(remaining - c) for c in coins ...)

That works great for small targets. But Python's C stack overflows
around depth 1000 (macOS default), and the curriculum's
test_large_target_no_recursion_limit calls `min_coins_topdown([1, 5,
10, 25], 10_000)` precisely to surface that. `sys.setrecursionlimit`
alone doesn't help because the OS thread stack is the actual ceiling.

This canonical solved version delivers the SAME memoized DP result
via bottom-up tabulation (still O(target * len(coins))). The dp
array IS the memoization table; the iteration order is the only
difference. A learner who writes the recursive form passes every
test EXCEPT test_large_target — at which point they reach for either
sys.setrecursionlimit + a bigger thread stack, or this iterative
shape. Both are valid; this shape is simpler and runs everywhere.
"""


def min_coins_topdown(coins: list[int], target: int) -> int:
    """Return the minimum number of coins to make target, or -1."""
    INF = float("inf")
    dp = [0] + [INF] * target
    for t in range(1, target + 1):
        for c in coins:
            if c <= t and dp[t - c] + 1 < dp[t]:
                dp[t] = dp[t - c] + 1
    return int(dp[target]) if dp[target] != INF else -1
