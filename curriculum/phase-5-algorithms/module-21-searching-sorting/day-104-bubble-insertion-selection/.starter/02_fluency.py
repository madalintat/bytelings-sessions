"""Rung 2: Fluency drill — fix the broken bubble sort.

Topic: bubble sort + how Python swaps.

`bubble_sort` doesn't actually sort — the swap line is wrong (it
overwrites instead of swapping). Use Python's tuple-swap idiom.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # TODO: this is not a swap — it makes both slots equal.
                arr[j] = arr[j + 1]
                arr[j + 1] = arr[j]
    return arr
