"""Rung 3: Guided — generate all permutations.

Topic: classic backtracking with breadcrumb-style used set.

Implement `permutations(arr)` returning every permutation of arr as
a list of lists. Order of permutations doesn't matter (tests
normalize), but each permutation must contain each input element
exactly once.

>>> sorted(permutations([1, 2, 3]))
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
>>> permutations([])
[[]]
>>> permutations([5])
[[5]]

Hints:
- Track which indices are used via a list of bools.
- Apply: append to partial, mark used.
- Undo:  pop from partial, unmark.
- Append a copy (`partial[:]`) when partial reaches len(arr).
"""


def permutations(arr: list) -> list[list]:
    raise NotImplementedError
