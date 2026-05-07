"""Rung 4: Solo.

Topic: 1D prefix sums in a tiny class — answer many range queries fast.

Implement the class `RangeSum` with this API:

    rs = RangeSum([3, 1, 4, 1, 5, 9, 2])
    rs.query(0, 3)   # 8   (sum of arr[0..2])
    rs.query(2, 5)   # 10  (sum of arr[2..4])
    rs.query(0, 7)   # 25  (whole array)
    rs.query(3, 3)   # 0   (empty range)

- The constructor builds a prefix-sum array in O(n).
- `query(a, b)` returns sum(arr[a:b]) in O(1).

Tests in 04_solo_test.py are HIDDEN.
"""


class RangeSum:
    def __init__(self, arr: list[int]):
        raise NotImplementedError

    def query(self, a: int, b: int) -> int:
        raise NotImplementedError
