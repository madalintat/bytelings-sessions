"""Rung 4: Solo — solved version.

quick_sort uses three-way partitioning with the middle element as
pivot. This avoids worst-case O(n^2) on already-sorted input (which
a first-element pivot would trigger). The three partitions are:
  less   — elements strictly smaller than pivot
  equal  — elements equal to pivot (handled in one shot)
  greater — elements strictly larger

Concatenating quick_sort(less) + equal + quick_sort(greater) gives a
sorted list. Returns a new list; input not mutated.
"""


def quick_sort(arr: list[int]) -> list[int]:
    """Sorted copy via three-way quicksort."""
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
