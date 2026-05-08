"""Rung 4: Solo — solved version.

insertion_sort_with_stats is standard insertion sort with a comparison
counter. Each time we evaluate `arr[j] > key` in the inner while-loop
we increment the counter — that is the one comparison per iteration.
The best case (already sorted) makes the while-loop execute exactly
once per outer step (i - 1 fails immediately after one check), giving
n - 1 total comparisons. The worst case (reverse sorted) makes it
execute i times per step, giving 1 + 2 + ... + (n-1) = n*(n-1)/2.
"""


def insertion_sort_with_stats(arr: list[int]) -> tuple[list[int], int]:
    """Return (sorted_list, comparison_count)."""
    arr = list(arr)
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons
