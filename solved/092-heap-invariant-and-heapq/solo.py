"""Rung 4: Solo — solved version.

merge_k_sorted uses a min-heap seeded with the first element from each
non-empty stream. Each heap entry is (value, stream_index, iterator).
The stream_index as a tiebreaker prevents Python from ever comparing
the raw iterator objects when two values are equal.

The algorithm runs in O(N log k) where N is the total number of
elements and k is the number of streams.
"""
import heapq
from typing import Iterable


def merge_k_sorted(streams: list[Iterable]) -> list:
    """Merge k sorted iterables into one sorted list."""
    heap: list = []
    iters = [iter(s) for s in streams]
    for idx, it in enumerate(iters):
        val = next(it, None)
        if val is not None:
            heapq.heappush(heap, (val, idx, it))

    result = []
    while heap:
        val, idx, it = heapq.heappop(heap)
        result.append(val)
        nxt = next(it, None)
        if nxt is not None:
            heapq.heappush(heap, (nxt, idx, it))
    return result
