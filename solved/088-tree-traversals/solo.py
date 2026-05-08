"""Rung 4: Solo implement — solved version.

right_view: use the levels() approach — for each level, take the last
element. This is the simplest and most readable implementation.
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


def right_view(root: Optional[TreeNode]) -> list:
    """Return the rightmost value at each level, top to bottom."""
    if root is None:
        return []
    q: deque = deque([root])
    result: list = []
    while q:
        level_size = len(q)
        last = None
        for _ in range(level_size):
            node = q.popleft()
            last = node.value
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(last)
    return result
