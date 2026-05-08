"""Rung 2: Fluency — solved version.

Undirected = symmetric. Every edge `(u, v)` records BOTH
`adj[u].append(v)` AND `adj[v].append(u)`. The starter forgot the
second line.

`defaultdict(list)` removes the "is this key present yet" question
— the first append creates the empty list automatically. We convert
to a plain dict at the end so the return type is predictable
(defaultdict has surprising lookup behavior in some contexts).
"""
from collections import defaultdict


def build_undirected(edges: list[tuple]) -> dict:
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return dict(adj)
