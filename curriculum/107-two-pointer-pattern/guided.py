"""Rung 3: Guided — pair-sum on a sorted list.

Topic: the classic two-pointer convergence.

Given a SORTED list `arr` and an int `target`, return a tuple
(i, j) of indices such that arr[i] + arr[j] == target and i < j.
If no such pair exists, return None.

>>> pair_sum([1, 2, 4, 7, 11], 9)
(1, 3)   # 2 + 7
>>> pair_sum([1, 2, 4, 7, 11], 100)
None
>>> pair_sum([], 5)
None

Hints:
- lo = 0, hi = len(arr) - 1
- While lo < hi:
    s = arr[lo] + arr[hi]
    if s == target: return (lo, hi)
    if s < target: lo += 1
    else: hi -= 1
- O(n), one pass.
"""


def pair_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    raise NotImplementedError
