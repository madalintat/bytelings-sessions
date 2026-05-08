"""Rung 3: Guided — solved version.

reverse_iter builds a new list by walking from the back with indices.
No mutation of the input; no slice shortcut.

tree_depth recurses: if a list has no sub-lists the depth is 1. Each
list item that is itself a list contributes depth 1 + its own depth.
The overall depth is the max across all children, defaulting to 1
for a flat list with no sub-lists.
"""


def reverse_iter(items: list) -> list:
    """Return a reversed copy of items. Iterative."""
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result


def tree_depth(items: list) -> int:
    """Return max nesting depth of a list-of-lists. Flat list -> 1.

    >>> tree_depth([1, 2, 3])
    1
    >>> tree_depth([1, [2, [3, [4]]]])
    4
    """
    max_child = 0
    for x in items:
        if isinstance(x, list):
            d = tree_depth(x)
            if d > max_child:
                max_child = d
    return 1 + max_child
