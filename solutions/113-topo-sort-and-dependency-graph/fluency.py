"""Rung 2: Fluency drill — fix Kahn's topo sort.

Topic: in-degree decrement on neighbors.

`topo_sort` returns a topological order. Currently it pulls every
in-degree-zero node up front and never decrements neighbors' in-
degrees, so it only finds the original sources. Fix the inner step.
"""
from collections import defaultdict, deque


def topo_sort(adj: dict) -> list:
    indeg = defaultdict(int)
    for u in adj:
        indeg.setdefault(u, 0)
        for v in adj[u]:
            indeg[v] += 1
    q = deque(n for n, d in indeg.items() if d == 0)
    out = []
    while q:
        u = q.popleft()
        out.append(u)
        for v in adj.get(u, []):
            # TODO: decrement in-degree of v; if it hits zero, enqueue v
            pass
    return out
