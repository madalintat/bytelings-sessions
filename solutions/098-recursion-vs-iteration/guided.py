"""Rung 3: Guided implement.

Topic: write each in its natural shape

`reverse_iter` reverses a list iteratively (single loop, O(n) memory).
`tree_depth` returns the maximum nesting depth of a list-of-lists,
recursively.

>>> reverse_iter([1, 2, 3, 4])
[4, 3, 2, 1]
>>> tree_depth([1, 2, 3])
1
>>> tree_depth([1, [2, [3, [4]]]])
4
>>> tree_depth([])
1

Hints:
- For `reverse_iter`: build a new list and append from the end, OR use
  two indices and swap. Either works. Don't use [::-1] — write it.
- For `tree_depth`: an empty list still counts as depth 1. The
  recursive case asks each child for its depth and takes the max + 1.
"""


def reverse_iter(items: list) -> list:
    raise NotImplementedError


def tree_depth(items: list) -> int:
    raise NotImplementedError
