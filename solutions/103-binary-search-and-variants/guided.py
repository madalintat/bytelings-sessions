"""Rung 3: Guided — implement lower_bound and upper_bound.

Topic: binary search variants for "first index where condition holds"

`lower_bound(arr, target)` — index of the first element >= target.
                            If all elements are < target, return len(arr).
`upper_bound(arr, target)` — index of the first element > target.
                            If all elements are <= target, return len(arr).

>>> lower_bound([1, 2, 4, 4, 4, 6], 4)
2
>>> upper_bound([1, 2, 4, 4, 4, 6], 4)
5
>>> upper_bound([1, 2, 4, 4, 4, 6], 4) - lower_bound([1, 2, 4, 4, 4, 6], 4)
3   # there are 3 fours

Hints:
- Same shape as bsearch but never returns "found" early.
- Use `lo, hi = 0, len(arr)` (note: hi is len, not len-1).
- Loop while `lo < hi`. Return `lo` at the end.
- For lower_bound: if arr[mid] < target, lo = mid + 1 else hi = mid.
- For upper_bound: if arr[mid] <= target, lo = mid + 1 else hi = mid.
"""


def lower_bound(arr: list[int], target: int) -> int:
    raise NotImplementedError


def upper_bound(arr: list[int], target: int) -> int:
    raise NotImplementedError
