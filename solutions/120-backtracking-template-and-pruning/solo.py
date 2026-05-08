"""Rung 4: Solo.

Topic: classic combinations with pruning.

Implement `combinations(n, k)` returning every k-element subset of
{1, 2, ..., n} as a sorted list of lists.

>>> combinations(4, 2)
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
>>> combinations(3, 0)
[[]]
>>> combinations(3, 3)
[[1, 2, 3]]

Hints:
- Backtrack starting at value 1, with a `partial` list.
- For each candidate v from `start` to n: append, recurse with
  start=v+1, undo.
- Base case: len(partial) == k → record a copy.
- Pruning to make this fast: if you'd run out of room — that is, if
  partial's length plus the remaining range can't reach k — skip.
  (e.g., if `n - v + 1 < k - len(partial)`, break out.)

Tests in 04_solo_test.py are HIDDEN.
"""


def combinations(n: int, k: int) -> list[list[int]]:
    raise NotImplementedError
