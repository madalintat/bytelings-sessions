"""Rung 4: Solo — solved version.

Course-schedule via topo sort. The classic shape: build a directed
graph where edge `b -> a` encodes "a depends on b" (so b must come
first). Run Kahn's algorithm. If we can produce all `n` courses in
the output, no cycle, return True.

The cycle-detection-by-count trick is the same as guided's: if the
output has fewer nodes than `n`, the missing ones are in a cycle.

Patterns: P-07 (accumulator-into-dict), P-27 (dfs-with-explicit-stack).
"""
from collections import defaultdict, deque


def can_finish(n: int, prereqs: list[tuple[int, int]]) -> bool:
    adj = defaultdict(list)
    indeg = [0] * n
    for a, b in prereqs:
        # b must come before a → edge b -> a
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return visited == n
