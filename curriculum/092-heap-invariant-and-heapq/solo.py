"""Rung 4: Solo implement.

Topic: write `merge_k_sorted(streams)` — merge k sorted iterables into one.

Given a list of iterables, each already sorted in ascending order,
return a single sorted list containing all values from all streams.

Example:
    merge_k_sorted([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

    merge_k_sorted([[1, 1, 1], [1, 1]])
    -> [1, 1, 1, 1, 1]

    merge_k_sorted([])     -> []
    merge_k_sorted([[]])   -> []

The heap-flavored algorithm:
    - Push the head of each stream onto a min-heap as (value, stream_index, iterator).
    - Pop the smallest. Emit the value. If that iterator has more, push its next.
    - Repeat until the heap is empty.

This is O(N log k) where N is total elements and k is the number of
streams — strictly faster than concatenate-and-sort when k is small
relative to N.

You can use Python's `heapq` here. The `(value, idx, ...)` tuple shape
matters: equal values fall back to comparing idx, never the iterator.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Iterable


def merge_k_sorted(streams: list[Iterable]) -> list:
    raise NotImplementedError
