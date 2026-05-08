"""Rung 4: Solo — solved version.

Reconstruction trick: track a `parent` dict alongside the distance
dict. When you set `dist[nb] = dist[u] + 1`, also record `parent[nb]
= u`. After BFS, walk parent backwards from goal to start, then
reverse.

Edge cases:
- start == goal: return [start] without traversing.
- goal unreachable: BFS finishes without ever setting parent[goal].

Patterns: P-10 (visit-set-for-dedup), P-26 (bfs-from-source).
"""
from collections import deque


def shortest_path(adj: dict, start, goal) -> list | None:
    if start == goal:
        return [start]
    parent: dict = {start: None}
    q = deque([start])
    while q:
        u = q.popleft()
        for nb in adj.get(u, []):
            if nb not in parent:
                parent[nb] = u
                if nb == goal:
                    # reconstruct
                    path = [goal]
                    cur = goal
                    while parent[cur] is not None:
                        cur = parent[cur]
                        path.append(cur)
                    path.reverse()
                    return path
                q.append(nb)
    return None
