"""Rung 2: Fluency drill — fix the broken two-pointer reverse.

Topic: classic opposite-ends two-pointer.

`reverse_in_place` is supposed to reverse a list in place using two
pointers walking inward and swapping. One of the pointer moves is
wrong, so it gets stuck or returns the wrong order. Fix it.

Returns the same list (modified in place) for convenience.
"""


def reverse_in_place(arr: list) -> list:
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        # TODO: hi must move too (the other direction)
    return arr
