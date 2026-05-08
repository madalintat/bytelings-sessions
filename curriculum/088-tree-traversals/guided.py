"""Rung 3: Guided implement — inorder, levelorder, and a height-by-BFS.

Topic: the three traversals you didn't write in rung 2, plus level-by-level work.
"""
from collections import deque
from typing import Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode]) -> list:
    """Left, node, right.

    For a BST, this returns values in sorted order. (We rely on that
    in tomorrow's day.)
    """
    # TODO
    raise NotImplementedError


def levelorder(root: Optional[TreeNode]) -> list:
    """Return values in BREADTH-first order — top row first, then next row.

    For:
            4
           / \
          2   6
         / \   \
        1   3   7
    -> [4, 2, 6, 1, 3, 7]

    Use a deque as a queue. Append children left-then-right.
    """
    # TODO
    raise NotImplementedError


def levels(root: Optional[TreeNode]) -> list[list]:
    """Return a list-of-lists, one inner list per tree level (top-down).

    levels(_sample_tree()) -> [[4], [2, 6], [1, 3, 7]]

    Trick: at the start of each outer iteration, take a snapshot of
    `len(queue)` — that's exactly how many nodes are in the current
    level. Pop that many; their children become the next level.
    """
    # TODO
    raise NotImplementedError
