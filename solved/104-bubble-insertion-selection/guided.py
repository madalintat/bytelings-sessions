"""Rung 3: Guided — solved version.

selection_sort: for each position i, scan arr[i+1:] for the minimum,
  then swap it into position i. O(n^2) comparisons, O(n) swaps.

insertion_sort: for each index i (starting at 1), take arr[i] as a
  "key" and shift larger elements rightward until the key fits in
  sorted order. O(n^2) worst case, O(n) best case (already sorted).

Both return a new list; the input is not mutated.
"""


def selection_sort(arr: list[int]) -> list[int]:
    """Sorted copy via selection sort."""
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: list[int]) -> list[int]:
    """Sorted copy via insertion sort."""
    arr = list(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
