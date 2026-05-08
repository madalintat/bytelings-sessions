"""Rung 2: Fluency — solved version.

After each swap the left pointer advances (lo += 1) but hi never
decreases. Both pointers must move inward simultaneously. Add
`hi -= 1` after the swap so the two pointers converge.
"""


def reverse_in_place(arr: list) -> list:
    """Reverse arr in place using opposite-ends two pointers."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1
    return arr
