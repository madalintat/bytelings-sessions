"""Rung 4: Solo — solved version.

Variable-size window with `running` sum. Expand the right edge each
step; whenever the window's sum is large enough, contract from the
left while it stays large enough, recording the smallest seen.

The `while running >= target` (not `if`) is critical — it shrinks
the window as much as possible at each step, otherwise we'd miss
strictly-smaller valid windows that share the same right edge.

O(n): each element is added once and removed at most once.

Patterns: P-06 (sliding-window).
"""

import math


def min_subarray_len(arr: list[int], target: int) -> int:
    left = 0
    running = 0
    best = math.inf
    for right, x in enumerate(arr):
        running += x
        while running >= target:
            best = min(best, right - left + 1)
            running -= arr[left]
            left += 1
    return 0 if best == math.inf else best
