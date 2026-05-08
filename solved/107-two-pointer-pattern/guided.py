"""Rung 3: Guided — solved version.

pair_sum uses the classic convergence: start lo at the left end, hi at
the right. If arr[lo] + arr[hi] == target, we found it. If the sum is
too small, advance lo (need a bigger left value). If too big, retreat
hi (need a smaller right value). Terminates in O(n).
"""


def pair_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    """Return (i, j) with arr[i] + arr[j] == target and i < j, or None."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return (lo, hi)
        if s < target:
            lo += 1
        else:
            hi -= 1
    return None
