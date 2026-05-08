"""Rung 2: Fluency drill — fix the off-by-one.

Topic: binary search, classic boundary bugs.

`bsearch` is supposed to return the index of `target` in a sorted
list, or -1 if not present. It's almost right but has one off-by-one
that makes it miss elements. Fix it.
"""


def bsearch(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo < hi:   # TODO: this loop terminates one step too early
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
