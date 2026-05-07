"""Rung 2: Fluency drill — fix DFS so it terminates on cyclic graphs.

Topic: DFS + visited set.

`reachable` is supposed to return the set of all nodes reachable from
`start`. It's missing the visited-set check, so on any cycle it
recurses forever. Add it.
"""


def reachable(adj: dict, start, visited: set | None = None) -> set:
    if visited is None:
        visited = set()
    visited.add(start)
    for nb in adj.get(start, []):
        # TODO: skip nb if it's already in visited
        reachable(adj, nb, visited)
    return visited
