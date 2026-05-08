"""Rung 3: Guided implement — sliding-window helpers.

Topic: deque(maxlen=k) for bounded sliding-window state.
"""
from collections import deque
from typing import Iterable


def last_n(stream: Iterable, n: int) -> list:
    """Return a list of the LAST n items from `stream`, in original order.

    If `stream` has fewer than n items, return all of them.

    >>> last_n([1, 2, 3, 4, 5], 3)
    [3, 4, 5]
    >>> last_n("abcde", 2)
    ['d', 'e']
    >>> last_n([1, 2], 5)
    [1, 2]

    Implementation hint: a deque(maxlen=n) drops the oldest for free.
    """
    # TODO
    raise NotImplementedError


def rolling_max(nums: list[int], k: int) -> list[int]:
    """Return a list where out[i] is max(nums[i:i+k]).

    For each window of size k as it slides one step right, return the
    maximum in that window. The result has len(nums) - k + 1 entries.

    >>> rolling_max([1, 3, 2, 5, 4], 3)
    [3, 5, 5]
    >>> rolling_max([7], 1)
    [7]
    >>> rolling_max([], 3)
    []

    A correct O(n*k) implementation is fine here. We'll see the
    O(n) deque-of-indices trick in Phase 5 — for now, a clear nested
    approach using a sliding-window deque is the goal.
    """
    # TODO
    raise NotImplementedError
