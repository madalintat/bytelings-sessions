"""Rung 3: Guided — implement merge_sort.

Topic: divide-and-conquer using the merge from rung 2.

Implement `merge_sort(arr)` as classic top-down merge sort:
- Base case: list of length 0 or 1 is already sorted.
- Recursive case: split in half, sort each, merge.

Return a NEW list; do not mutate the input.

>>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
[1, 1, 2, 3, 4, 5, 6, 9]
>>> merge_sort([])
[]
>>> merge_sort([1])
[1]

Hints:
- You may either reimplement merge here, or (cleaner) define a small
  helper inside the function. Do not import from rung 2.
- mid = len(arr) // 2. left = arr[:mid]. right = arr[mid:].
"""


def merge_sort(arr: list[int]) -> list[int]:
    raise NotImplementedError
