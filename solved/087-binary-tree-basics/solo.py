"""Rung 4: Solo implement — solved version.

same_shape: two trees have the same shape iff both are None (base case)
or both are non-None and their left/right subtrees match recursively.
mirror: swap left and right recursively; mutates in place and returns root.
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
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return same_shape(a.left, b.left) and same_shape(a.right, b.right)


def mirror(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = mirror(root.right), mirror(root.left)
    return root
