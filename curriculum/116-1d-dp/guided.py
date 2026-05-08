"""Rung 3: Guided — Longest Increasing Subsequence (LIS).

Topic: classic 1D DP with a quadratic recurrence.

Given a list of ints, return the length of the longest STRICTLY
increasing subsequence (not necessarily contiguous).

>>> lis([10, 9, 2, 5, 3, 7, 101, 18])
4    # [2, 3, 7, 101]
>>> lis([])
0
>>> lis([5, 5, 5])
1    # strict — duplicates don't extend
>>> lis([1, 2, 3, 4])
4

Hints:
- dp[i] = length of LIS ending EXACTLY at index i.
- dp[i] = 1 + max(dp[j] for j < i if arr[j] < arr[i]) if any j; else 1.
- Final answer: max(dp). Empty array → 0.
- O(n^2). The O(n log n) version uses binary search but is optional.
"""


def lis(arr: list[int]) -> int:
    raise NotImplementedError
