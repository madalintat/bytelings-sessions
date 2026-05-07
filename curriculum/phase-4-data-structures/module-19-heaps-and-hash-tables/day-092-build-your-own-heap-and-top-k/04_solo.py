"""Rung 4: Solo implement.

Topic: write `top_k(stream, k)` — the k largest values from an iterable.

Given an iterable `stream` and an int `k >= 0`, return the k LARGEST
values, in DESCENDING order. If `k` >= len(stream), return all values
sorted descending.

You MUST do it in O(n log k) time and O(k) space — that's the whole
point of this exercise. Use heapq (or your own MinHeap from rung 3,
either is fine), with a min-heap of size k as the "current top-k"
running set. When you see a new item:
    - if heap has < k entries: push it
    - elif item > heap[0]: heapreplace it in
After the stream, sort the heap in DESCENDING order and return.

Examples:
    top_k([5, 1, 9, 3, 7, 2], 3) -> [9, 7, 5]
    top_k([], 3)                 -> []
    top_k([1, 2], 5)             -> [2, 1]
    top_k([1, 2, 3, 4], 0)       -> []

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Iterable


def top_k(stream: Iterable, k: int) -> list:
    raise NotImplementedError
