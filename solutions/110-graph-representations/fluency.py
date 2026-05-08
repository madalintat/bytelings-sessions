"""Rung 2: Fluency drill — fix the undirected graph builder.

Topic: directed vs undirected adjacency lists.

`build_undirected` takes a list of edges (pairs) and should return an
adjacency dict where each edge is recorded in BOTH directions
(undirected = symmetric). Currently it only records one direction.
"""
from collections import defaultdict


def build_undirected(edges: list[tuple]) -> dict:
    """Each edge is (u, v); add v to adj[u] AND u to adj[v]."""
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        # TODO: missing the symmetric line
    return dict(adj)
