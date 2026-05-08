"""Rung 4: Solo — solved version.

3-coloring DFS for cycle detection in directed graphs.

WHITE = not yet visited (default for absent keys).
GRAY = currently on the active DFS path.
BLACK = fully explored, no cycle through it.

Finding an edge to a GRAY node = cycle (back-edge to an ancestor on
the current path). Finding a BLACK node = already proven safe; skip.

Edge case: self-loop `1 -> 1`. When DFS on 1 examines neighbor 1,
1 is GRAY (just colored before iterating its neighbors). Returns
True. Good.

Patterns: P-10 (visit-set-for-dedup), P-27 (dfs-with-explicit-stack)
— this implementation uses RECURSIVE DFS (cleaner here because the
3-color state attaches naturally to call frames).
"""

WHITE, GRAY, BLACK = 0, 1, 2


def has_cycle(adj: dict) -> bool:
    color: dict = {}

    def dfs(u) -> bool:
        color[u] = GRAY
        for nb in adj.get(u, []):
            c = color.get(nb, WHITE)
            if c == GRAY:
                return True
            if c == WHITE and dfs(nb):
                return True
        color[u] = BLACK
        return False

    for node in adj:
        if color.get(node, WHITE) == WHITE:
            if dfs(node):
                return True
    return False
