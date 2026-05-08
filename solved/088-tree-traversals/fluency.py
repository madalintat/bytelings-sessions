"""Rung 2: Fluency drill — solved version.

preorder: visit (append) BEFORE the two recursive calls.
postorder: visit (append) AFTER both recursive calls.
"""
from typing import Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


def preorder(root: Optional[TreeNode]) -> list:
    """Return values in PRE-order: node, left, right."""
    out: list = []

    def walk(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        out.append(node.value)
        walk(node.left)
        walk(node.right)

    walk(root)
    return out


def postorder(root: Optional[TreeNode]) -> list:
    """Return values in POST-order: left, right, node."""
    out: list = []

    def walk(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        walk(node.left)
        walk(node.right)
        out.append(node.value)

    walk(root)
    return out
