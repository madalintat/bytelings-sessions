"""Rung 4: Solo implement — solved version.

Classic two-pointer merge: advance whichever pointer points to the
smaller value, appending to the output list. Drain whichever list
still has elements when the other is exhausted. O(n + m) time.
"""


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    out: list[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
