"""Rung 4: Solo implement.

Topic: walk consecutive pairs of a list

Implement `running_diffs(items)`:

- Given a list of numbers, return a list of (b - a) for each
  consecutive pair (a, b).
- For a list of length n, returns a list of length n - 1.
- Empty list -> []. Single-item list -> [].

Examples:
    running_diffs([10, 12, 9, 14])  -> [2, -3, 5]
    running_diffs([1])              -> []
    running_diffs([])               -> []

Hint: zip(items, items[1:]) gives you each consecutive pair.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-13 (enumerate-for-index), P-14 (zip-parallel-walk), P-15 (unpacking-into-named).
"""


def running_diffs(items: list[float]) -> list[float]:
    raise NotImplementedError
