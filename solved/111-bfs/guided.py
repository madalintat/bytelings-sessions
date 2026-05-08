"""Rung 3: Guided — solved version.

The dict `dist` doubles as the visited set: a node is "visited" iff
it's in `dist`. This is cleaner than maintaining a separate visited
set because the value (its distance) is what we needed anyway.

Standard BFS layer-by-layer: each pop is a node at distance d, every
unseen neighbor is at distance d + 1.
"""
from collections import deque


def shortest_distances(adj: dict, start) -> dict:
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for nb in adj.get(u, []):
            if nb not in dist:
                dist[nb] = dist[u] + 1
                q.append(nb)
    return dist
