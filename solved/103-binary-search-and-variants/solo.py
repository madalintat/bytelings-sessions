"""Rung 4: Solo — solved version.

max_requests builds a prefix-sum array (length n+1, prefix[k] = sum
of the k cheapest requests). Then binary-searches for the largest k
such that prefix[k] <= capacity. This is an upper-bound-style query:
we want the largest index where the prefix sum does not exceed the
capacity, which is equivalent to upper_bound(prefix, capacity) - 1.
"""


def max_requests(costs: list[int], capacity: int) -> int:
    """Largest k such that costs[0] + ... + costs[k-1] <= capacity."""
    n = len(costs)
    # Build prefix sums. prefix[k] = sum of first k costs.
    prefix = [0] * (n + 1)
    for i, c in enumerate(costs):
        prefix[i + 1] = prefix[i] + c

    # Binary-search: largest k with prefix[k] <= capacity.
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2  # upper mid to avoid infinite loop
        if prefix[mid] <= capacity:
            lo = mid
        else:
            hi = mid - 1
    return lo
