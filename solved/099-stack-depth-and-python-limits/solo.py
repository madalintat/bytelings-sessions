"""Rung 4: Solo — solved version.

max_value uses an explicit stack of nodes. We start with the root,
then repeatedly pop a node, update the running maximum, and push its
children. This is iterative DFS with no recursion limit risk.
"""


def max_value(node: dict) -> int:
    """Return the largest value in a tree dict. Iterative stack DFS.

    >>> max_value({"value": 5, "children": []})
    5
    >>> max_value({"value": 1, "children": [{"value": 9, "children": []}]})
    9
    """
    best = node["value"]
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur["value"] > best:
            best = cur["value"]
        stack.extend(cur["children"])
    return best
