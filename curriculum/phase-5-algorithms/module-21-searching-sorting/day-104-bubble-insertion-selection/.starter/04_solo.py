"""Rung 4: Solo.

Topic: count comparisons in insertion sort.

Implement `insertion_sort_with_stats(arr)` that returns a tuple
(sorted_list, comparisons) where `comparisons` is the number of times
you compared two list elements via `<` or `>` in the inner loop.

This lets you experimentally see insertion sort's best-case (already
sorted → ~n-1 comparisons) and worst-case (reverse sorted → ~n^2/2).

>>> insertion_sort_with_stats([1, 2, 3, 4])
([1, 2, 3, 4], 3)
>>> insertion_sort_with_stats([4, 3, 2, 1])
([1, 2, 3, 4], 6)

Tests in 04_solo_test.py are HIDDEN.
"""


def insertion_sort_with_stats(arr: list[int]) -> tuple[list[int], int]:
    raise NotImplementedError
