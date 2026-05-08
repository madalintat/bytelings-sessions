"""Rung 2: Fluency — solved version.

The starter formula `p[a] - p[b - 1]` is a classic indexing slip.
The right formula for prefix-sum range query (right-exclusive) is:

    sum(arr[a:b]) == p[b] - p[a]

Reading: "sum up to but not including index b" minus "sum up to but
not including index a" gives the sum from a (inclusive) to b
(exclusive). This is why p has length len(arr) + 1: p[0] is 0 (the
empty prefix), p[n] is sum(arr).
"""


def build_prefix(arr: list[int]) -> list[int]:
    p = [0]
    for x in arr:
        p.append(p[-1] + x)
    return p


def range_sum(p: list[int], a: int, b: int) -> int:
    return p[b] - p[a]
