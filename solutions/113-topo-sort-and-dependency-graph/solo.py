"""Rung 4: Solo.

Topic: course schedule — can you take all courses?

You have `n` courses (numbered 0 to n-1) and a list of prerequisite
pairs `(a, b)` meaning "must take b before a." (Read it as: a depends
on b.)

Implement `can_finish(n, prereqs)` returning True iff there's a valid
order to take all courses (i.e., the graph has no cycle).

>>> can_finish(2, [(1, 0)])
True
>>> can_finish(2, [(1, 0), (0, 1)])
False
>>> can_finish(4, [(1, 0), (2, 1), (3, 2)])
True

Hints:
- Build the directed graph: an edge from b to a means "b enables a."
- Apply topo-sort-style cycle detection. If you can produce a full
  ordering (len == n), True; else False.

Tests in 04_solo_test.py are HIDDEN.
"""


def can_finish(n: int, prereqs: list[tuple[int, int]]) -> bool:
    raise NotImplementedError
