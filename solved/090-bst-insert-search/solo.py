"""Rung 4: Solo — solved version.

The BST-aware traversal: at each node, recurse into the LEFT subtree
ONLY if the node's value is greater than `lo` (otherwise everything
in the left subtree is below lo and skippable). Same for RIGHT and
`hi`. This prunes entire subtrees that can't contain anything in
[lo, hi], giving O(k + log n) expected time on a balanced tree where
k is the result size, vs. O(n) for the naive approach.

The recursion's order ensures the result list is sorted ascending:
left subtree (smaller values) first, then self, then right subtree.
"""


def range_query(root, lo, hi) -> list:
    out: list = []

    def visit(node) -> None:
        if node is None:
            return
        if node.value > lo:
            visit(node.left)
        if lo <= node.value <= hi:
            out.append(node.value)
        if node.value < hi:
            visit(node.right)

    visit(root)
    return out
