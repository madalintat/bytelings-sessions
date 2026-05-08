"""Rung 4: Solo.

Topic: implement quicksort.

Implement `quick_sort(arr)` using the simple "three-way partition"
style:
- If len(arr) <= 1: return arr.
- Pick a pivot (arr[len(arr) // 2] is fine; random.choice also fine).
- Build less = [x for x in arr if x < pivot],
        equal = [x for x in arr if x == pivot],
        greater = [x for x in arr if x > pivot].
- Return quick_sort(less) + equal + quick_sort(greater).

Return a NEW list; do not mutate the input.

>>> quick_sort([3, 1, 4, 1, 5, 9, 2, 6])
[1, 1, 2, 3, 4, 5, 6, 9]

Tests in 04_solo_test.py are HIDDEN.
"""


def quick_sort(arr: list[int]) -> list[int]:
    raise NotImplementedError
