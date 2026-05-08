"""Rung 2: Fluency drill — fix the mislabeled traversals.

Topic: where the visit() call lives in pre/in/post.
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
        # TODO: this is INORDER (visit between recursions). Move the
        # append to be BEFORE both recursive calls.
        walk(node.left)
        out.append(node.value)
        walk(node.right)

    walk(root)
    return out


def postorder(root: Optional[TreeNode]) -> list:
    """Return values in POST-order: left, right, node."""
    out: list = []

    def walk(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        # TODO: this is PREORDER. Move the append to be AFTER both
        # recursive calls.
        out.append(node.value)
        walk(node.left)
        walk(node.right)

    walk(root)
    return out
