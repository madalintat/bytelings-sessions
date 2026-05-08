"""Rung 4: Solo — solved version.

Wrap the prefix-sum array in a class. Constructor builds the prefix
in O(n). `query(a, b)` returns `p[b] - p[a]` in O(1).

The `query(3, 3)` empty-range case returns 0 because p[3] - p[3] is
0. No special-casing needed.

Pre-build vs. lazy: we eagerly build the full prefix array because
range queries are expected to be many. For a one-shot query, prefix
sums are overkill.
"""


class RangeSum:
    def __init__(self, arr: list[int]):
        self._p = [0]
        for x in arr:
            self._p.append(self._p[-1] + x)

    def query(self, a: int, b: int) -> int:
        return self._p[b] - self._p[a]
