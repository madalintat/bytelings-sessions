"""Rung 3: Guided — BFS shortest-path distances.

Topic: BFS gives you shortest hop-count for free.

Implement `shortest_distances(adj, start)` that returns a dict mapping
each reachable node to its shortest distance from `start` (in edges).
Unreachable nodes are NOT in the dict.

>>> adj = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": [], "X": []}
>>> shortest_distances(adj, "A")
{'A': 0, 'B': 1, 'C': 1, 'D': 2}

Hints:
- Start with dist = {start: 0} and a deque([start]).
- For each popped u, for each neighbor nb, if nb not in dist:
    dist[nb] = dist[u] + 1
    enqueue nb.
- Why no separate `visited`? Because being in `dist` IS being visited.
"""
from collections import deque


def shortest_distances(adj: dict, start) -> dict:
    raise NotImplementedError
