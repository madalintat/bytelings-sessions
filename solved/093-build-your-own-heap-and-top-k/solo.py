"""Rung 4: Solo — solved version.

top_k maintains a min-heap of at most k items. For each new item:
  - if the heap has fewer than k elements, push unconditionally.
  - otherwise, if the item beats the current minimum (heap[0]), replace
    the minimum with heapreplace (cheaper than pop + push).

After the stream, the heap contains the k largest values. Sorting it
in descending order (sorted(..., reverse=True)) gives the final answer.

Time: O(n log k). Space: O(k).
"""
import heapq
from typing import Iterable


def top_k(stream: Iterable, k: int) -> list:
    """Return the k largest values from stream, in descending order."""
    if k <= 0:
        return []
    heap: list = []
    for item in stream:
        if len(heap) < k:
            heapq.heappush(heap, item)
        elif item > heap[0]:
            heapq.heapreplace(heap, item)
    return sorted(heap, reverse=True)
