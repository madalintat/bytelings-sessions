"""Rung 3: Guided implement — solved version.

count_leaves: None -> 0; leaf (both children None) -> 1; otherwise sum
left + right subtrees.
max_value: None -> None; compare current with left/right max, ignoring None.
is_balanced: a clean (balanced, height) helper avoids recomputing height.
"""
from typing import Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


def count_leaves(root: Optional[TreeNode]) -> int:
    """Return the number of leaves (nodes with no children)."""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def max_value(root: Optional[TreeNode]) -> Optional[int]:
    """Return the maximum integer value in the tree, or None if empty."""
    if root is None:
        return None
    candidates = [root.value]
    left_max = max_value(root.left)
    right_max = max_value(root.right)
    if left_max is not None:
        candidates.append(left_max)
    if right_max is not None:
        candidates.append(right_max)
    return max(candidates)


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Return True if the tree is height-balanced at every node."""
    def check(node: Optional[TreeNode]) -> tuple[bool, int]:
        """Return (is_balanced, height). height uses -1 for None."""
        if node is None:
            return True, -1
        lb, lh = check(node.left)
        if not lb:
            return False, 0
        rb, rh = check(node.right)
        if not rb:
            return False, 0
        balanced = abs(lh - rh) <= 1
        return balanced, 1 + max(lh, rh)

    ok, _ = check(root)
    return ok
