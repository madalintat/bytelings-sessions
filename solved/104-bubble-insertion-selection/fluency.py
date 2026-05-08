"""Rung 2: Fluency — solved version.

The swap line `arr[j] = arr[j+1]; arr[j+1] = arr[j]` first overwrites
arr[j] with arr[j+1], then tries to write the now-lost value back.
Python's tuple-swap idiom `arr[j], arr[j+1] = arr[j+1], arr[j]`
evaluates both right-hand sides before any assignment happens.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """Return a sorted copy using bubble sort."""
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
