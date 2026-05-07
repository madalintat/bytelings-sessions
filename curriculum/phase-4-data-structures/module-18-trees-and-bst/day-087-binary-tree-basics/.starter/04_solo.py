"""Rung 4: Solo implement.

Topic: write `same_shape(a, b)` and `mirror(root)`.

`same_shape(a, b)` returns True iff the two trees have IDENTICAL
shape (matching None positions) — values are ignored. None and a
single leaf have the same shape only as None or as a single leaf
respectively.

Examples:
    same_shape(None, None)                                 -> True
    same_shape(TreeNode(1), TreeNode(99))                  -> True   # values ignored
    same_shape(TreeNode(1, TreeNode(2)), TreeNode(1))      -> False
    same_shape(TreeNode(1, TreeNode(2)), TreeNode(1, TreeNode(2)))  -> True

`mirror(root)` returns the root of a tree whose shape is the
horizontal mirror image of `root`. May mutate or rebuild — your call.
For these tests we'll check via in-order traversal, so any correct
mirror works.

Examples:
    mirror(None)                              -> None
    mirror(TreeNode(1)) -> TreeNode(1)
    Mirror of:               becomes:
        1                       1
       / \                     / \
      2   3                   3   2
     /                             \
    4                               4

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


def same_shape(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    raise NotImplementedError


def mirror(root: Optional[TreeNode]) -> Optional[TreeNode]:
    raise NotImplementedError
