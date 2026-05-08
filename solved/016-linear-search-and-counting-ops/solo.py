"""Rung 4: Solo — solved version.

`find_pair_with_sum` uses a nested loop (O(n^2) naive approach as
specified for this rung). The outer loop fixes `i` from 0 to n-2; the
inner loop checks every j > i. We return immediately on the first
hit, which guarantees the smallest i and, for a fixed i, the smallest j.

Day 22 will show how to improve this to O(n) with a set of complements.
For now, the O(n^2) approach is explicit and correct.
"""


def find_pair_with_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
