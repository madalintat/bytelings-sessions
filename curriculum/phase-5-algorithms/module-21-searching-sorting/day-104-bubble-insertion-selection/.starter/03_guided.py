"""Rung 3: Guided — implement selection_sort and insertion_sort.

Topic: two more O(n^2) sorts, in their natural shape.

Both must:
- Return a NEW sorted list (do not mutate the input).
- Sort ascending.

>>> selection_sort([3, 1, 4, 1, 5])
[1, 1, 3, 4, 5]
>>> insertion_sort([3, 1, 4, 1, 5])
[1, 1, 3, 4, 5]

Hints:
- selection_sort: outer loop picks position i. Inner loop scans
  arr[i+1..end] for the minimum. Swap into position i.
- insertion_sort: take each item arr[i] (i from 1..n-1) and shift it
  left through the already-sorted prefix until its left neighbor is
  smaller (or you hit index 0).
"""


def selection_sort(arr: list[int]) -> list[int]:
    raise NotImplementedError


def insertion_sort(arr: list[int]) -> list[int]:
    raise NotImplementedError
