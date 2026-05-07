"""Rung 4: Solo.

Topic: smallest contiguous subarray with sum >= target (positive ints).

Given a list `arr` of positive ints and an int `target`, return the
length of the smallest contiguous subarray whose sum is at least
`target`. Return 0 if no such subarray exists.

>>> min_subarray_len([2, 3, 1, 2, 4, 3], 7)
2     # [4, 3]
>>> min_subarray_len([1, 1, 1, 1], 100)
0
>>> min_subarray_len([1, 4, 4], 4)
1

Hints (variable-size sliding window):
- left = 0; running_sum = 0; best = infinity.
- for right, x in enumerate(arr):
    running_sum += x
    while running_sum >= target:
        best = min(best, right - left + 1)
        running_sum -= arr[left]
        left += 1
- Return 0 if best is still infinity.

Tests in 04_solo_test.py are HIDDEN.
"""


def min_subarray_len(arr: list[int], target: int) -> int:
    raise NotImplementedError
