"""Rung 2: Fluency — solved version.

Kahn's algorithm: when you pop a node `u`, every neighbor `v` loses
one prerequisite. Decrement `indeg[v]`; if it hits zero, `v` is now
ready, enqueue it.

The starter forgot the inner step, so only the original sources came
out and everything depending on them stayed unprocessed.
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
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return out
