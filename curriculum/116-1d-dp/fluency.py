"""Rung 2: Fluency drill — fix Kadane's.

Topic: 1D DP, max subarray sum.

`max_subarray` should return the max sum of a contiguous subarray.
The recurrence is wrong — it always extends, never starts fresh,
which fails for arrays with leading negatives.
"""


def max_subarray(arr: list[int]) -> int:
    if not arr:
        return 0
    best = cur = arr[0]
    for x in arr[1:]:
        # TODO: cur should be max(x, cur + x), not always cur + x
        cur = cur + x
        if cur > best:
            best = cur
    return best
