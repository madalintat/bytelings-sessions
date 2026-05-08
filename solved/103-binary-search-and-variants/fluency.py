"""Rung 2: Fluency — solved version.

The loop condition `while lo < hi` exits when lo == hi, which means
the element at that final index is never checked. Change to
`while lo <= hi` so the single-element case is handled and the search
can return a hit on the last remaining candidate.
"""


def bsearch(arr: list[int], target: int) -> int:
    """Return the index of target in sorted arr, or -1 if absent."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
