"""Rung 2: Fluency — solved version.

Without the visited-set check, any cycle (or any node with multiple
incoming edges) loops forever. Add the guard `if nb not in visited`
before recursing.

The default `visited=None` + `if visited is None: visited = set()`
idiom is the standard fix for the mutable-default-argument trap (see
Day 24, P-24 sentinel-default).
"""


def reachable(adj: dict, start, visited: set | None = None) -> set:
    if visited is None:
        visited = set()
    visited.add(start)
    for nb in adj.get(start, []):
        if nb not in visited:
            reachable(adj, nb, visited)
    return visited
