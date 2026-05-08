"""Rung 3: Guided — solved version.

merge_sort splits the input in half, recursively sorts each half, then
merges the two sorted halves. A local merge helper avoids importing
from rung 2. Base case: a list of 0 or 1 element is already sorted.
Returns a new list; the input is not mutated.
"""


def merge_sort(arr: list[int]) -> list[int]:
    """Sorted copy via top-down merge sort. O(n log n)."""
    if len(arr) <= 1:
        return list(arr)

    def _merge(a, b):
        out = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                out.append(a[i]); i += 1
            else:
                out.append(b[j]); j += 1
        out += a[i:]
        out += b[j:]
        return out

    mid = len(arr) // 2
    return _merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
