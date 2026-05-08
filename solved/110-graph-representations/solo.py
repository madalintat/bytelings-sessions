"""Rung 4: Solo — solved version.

`build_weighted` mirrors the undirected-builder shape, but: (a) only
adds u→v (directed), (b) stores tuples `(neighbor, weight)`. We use
a regular dict and `setdefault(u, [])` so Python's insertion-order
guarantee (3.7+) preserves the order edges appeared in.

`total_weight` sums the second element of every (neighbor, weight)
pair across every node's adjacency list. Since edges are directed,
each is counted exactly once.

Patterns: P-10 (visit-set-for-dedup), P-27 (dfs-with-explicit-stack)
— the patterns are pre-tagged for the day, not directly exercised
by these particular helpers.
"""


def build_weighted(edges: list[tuple]) -> dict:
    adj: dict = {}
    for u, v, w in edges:
        adj.setdefault(u, []).append((v, w))
    return adj


def total_weight(adj: dict) -> int:
    return sum(w for neighbors in adj.values() for _, w in neighbors)
