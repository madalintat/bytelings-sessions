"""Rung 3: Guided — solved version.

Two converters, exact mirrors of each other. The `range(n)`-default
in `matrix_to_adj` ensures every node appears in the dict (with
empty list if it has no out-edges). Otherwise a node with zero
outgoing edges would be silently absent.

`adj_to_matrix` builds an n×n zero matrix, then sets `m[i][j] = 1`
for every edge. The double comprehension `[[0] * n for _ in
range(n)]` is the canonical fresh-rows pattern; `[[0]*n] * n` would
share the same list across all rows (classic mutability trap from
Day 4).
"""


def matrix_to_adj(m: list[list[int]]) -> dict[int, list[int]]:
    n = len(m)
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if m[i][j]:
                adj[i].append(j)
    return adj


def adj_to_matrix(adj: dict[int, list[int]], n: int) -> list[list[int]]:
    m = [[0] * n for _ in range(n)]
    for u, neighbors in adj.items():
        for v in neighbors:
            m[u][v] = 1
    return m
