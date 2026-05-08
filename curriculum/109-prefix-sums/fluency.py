"""Rung 2: Fluency drill — fix the prefix-sum off-by-one.

Topic: prefix sums for O(1) range queries.

`build_prefix` is correct. `range_sum(p, a, b)` should return the sum
of arr[a..b-1] (right-exclusive, like Python slicing) — but the
indexing is off. Fix it.
"""


def build_prefix(arr: list[int]) -> list[int]:
    """Return p where p[i] = sum(arr[:i]). len(p) == len(arr) + 1."""
    p = [0]
    for x in arr:
        p.append(p[-1] + x)
    return p


def range_sum(p: list[int], a: int, b: int) -> int:
    """Sum of arr[a..b-1] using prefix sums. Equivalent to sum(arr[a:b])."""
    # TODO: indices are wrong — fix the formula
    return p[a] - p[b - 1]
