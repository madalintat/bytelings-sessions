"""Rung 4: Solo.

Topic: BFS shortest-path RECONSTRUCTION (not just length).

Implement `shortest_path(adj, start, goal)` that returns the actual
list of nodes on a shortest path from start to goal, inclusive on
both ends. Returns None if goal is unreachable. If start == goal,
returns [start].

>>> adj = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}
>>> shortest_path(adj, "A", "E")
['A', 'B', 'D', 'E']    # or ['A', 'C', 'D', 'E'] — either is valid

The standard trick: track a `parent` dict during BFS. When you set
dist[nb] = dist[u] + 1, also set parent[nb] = u. After BFS, walk
parent from goal back to start, reverse, return.

Tests in 04_solo_test.py are HIDDEN — they accept any valid shortest
path of the right length.
"""


def shortest_path(adj: dict, start, goal) -> list | None:
    raise NotImplementedError
