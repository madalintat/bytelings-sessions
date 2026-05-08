"""Rung 3: Guided implement — solved version.

inorder: left, node, right (recursive).
levelorder: iterative BFS with a deque — popleft, append left/right.
levels: snapshot len(queue) at the start of each outer loop to know
how many nodes belong to the current level.
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
    """Left, node, right."""
    out: list = []

    def walk(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        walk(node.left)
        out.append(node.value)
        walk(node.right)

    walk(root)
    return out


def levelorder(root: Optional[TreeNode]) -> list:
    """Return values in breadth-first order."""
    if root is None:
        return []
    q: deque = deque([root])
    out: list = []
    while q:
        node = q.popleft()
        out.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


def levels(root: Optional[TreeNode]) -> list[list]:
    """Return a list-of-lists, one inner list per tree level (top-down)."""
    if root is None:
        return []
    q: deque = deque([root])
    result: list[list] = []
    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(current_level)
    return result
