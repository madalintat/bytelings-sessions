"""Rung 3: Guided implement — solved version.

last_n: consume the stream into a deque(maxlen=n) — the oldest items
are auto-evicted, leaving exactly the last n (or fewer).
rolling_max: slide a window of size k, take max of the window contents.
O(n*k) is acceptable here; the O(n) deque-of-indices version comes later.
"""
from collections import deque
from typing import Iterable


def last_n(stream: Iterable, n: int) -> list:
    """Return a list of the LAST n items from `stream`, in original order."""
    buf: deque = deque(maxlen=n)
    for item in stream:
        buf.append(item)
    return list(buf)


def rolling_max(nums: list[int], k: int) -> list[int]:
    """Return a list where out[i] is max(nums[i:i+k])."""
    if not nums or k <= 0 or k > len(nums):
        return []
    window: deque[int] = deque(maxlen=k)
    out: list[int] = []
    for num in nums:
        window.append(num)
        if len(window) == k:
            out.append(max(window))
    return out
