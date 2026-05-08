"""Rung 3: Guided — solved version.

Cycle detection by counting: if Kahn's algorithm produces fewer
nodes than the graph contains, the missing ones are stuck in a
cycle (every cycle has all in-degrees > 0 forever).

`packages = set` collects every name that appears anywhere in deps,
either as prereq or dependent — necessary because a package with no
prereqs and no dependents (a hermit) still has to appear in the
output if it's mentioned.
"""
from collections import defaultdict, deque


def build_order(deps: list[tuple]) -> list:
    adj = defaultdict(list)
    indeg: dict = {}
    packages: set = set()
    for prereq, dependent in deps:
        adj[prereq].append(dependent)
        packages.add(prereq)
        packages.add(dependent)
        indeg.setdefault(prereq, 0)
        indeg[dependent] = indeg.get(dependent, 0) + 1
    for p in packages:
        indeg.setdefault(p, 0)
    q = deque(p for p in packages if indeg[p] == 0)
    out = []
    while q:
        u = q.popleft()
        out.append(u)
        for v in adj.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(out) != len(packages):
        raise ValueError("cycle detected")
    return out
