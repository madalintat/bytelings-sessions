"""Rung 4: Solo.

Topic: binary search a *condition*, not a value.

You have a server with a fixed CPU budget. Each request costs `cost`
CPU. The server is rated for `capacity` total CPU per second.

Given a sorted list `costs` of per-request costs (ascending), find
the largest count of requests you can serve such that their total
cost is <= capacity. (Pick the cheapest ones first — they're at the
front of the sorted list, so this is just: how big a prefix sums to
<= capacity?)

Solve in O(log n) using binary search on the prefix-sum boundary.

>>> max_requests([1, 2, 3, 4, 5], 6)   # 1+2+3 = 6, plus 4 would be 10
3
>>> max_requests([10, 20, 30], 5)
0
>>> max_requests([1, 1, 1, 1], 100)
4

Hints:
- Build prefix sums first: prefix[i] = sum of costs[0..i-1].
- Then binary-search the largest k such that prefix[k] <= capacity.
- That's an upper-bound-style query.

Tests in 04_solo_test.py are HIDDEN.
"""


def max_requests(costs: list[int], capacity: int) -> int:
    raise NotImplementedError
