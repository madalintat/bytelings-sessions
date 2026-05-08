r"""Rung 4: Solo implement.

Topic: write `right_view(root)` — the right side of the tree.

Imagine standing to the RIGHT of the tree and looking at it. You see
the rightmost node at each level. Return those values, top to bottom.

For:
        1
       / \
      2   3
     / \   \
    4   5   6

You'd see [1, 3, 6].

A second example:
        1
       /
      2
     /
    3

You'd see [1, 2, 3] (each level has only one node).

Spec:
    right_view(None)         -> []
    right_view(TreeNode(1))  -> [1]

Hint: levels() from rung 3 makes this trivial — for each level, the
last element. But you can also do it with a single BFS, taking the
last node popped from each level.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


def right_view(root: Optional[TreeNode]) -> list:
    raise NotImplementedError
