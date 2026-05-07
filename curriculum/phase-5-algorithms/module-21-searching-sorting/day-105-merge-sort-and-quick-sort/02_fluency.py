"""Rung 2: Fluency drill — fix the merge.

Topic: merging two sorted lists, the heart of merge sort.

`merge` is supposed to merge two sorted lists into one sorted list
in O(n) time. It works on some inputs but drops elements at the end
when one list runs out. Find the missing piece.
"""


def merge(a: list[int], b: list[int]) -> list[int]:
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    # TODO: when one list is exhausted, the leftovers from the other
    # must still be appended. Currently they're silently dropped.
    return out
