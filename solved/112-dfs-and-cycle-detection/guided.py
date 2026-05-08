"""Rung 3: Guided — solved version.

Connected components: try every node as a starting point. If we
haven't seen it yet, run DFS from it (marking everything reachable
as visited). Each successful start is one new component.

Recursive DFS works fine for the test sizes here. For very deep
graphs, the explicit-stack form (P-27) avoids Python's recursion
limit:

    stack = [node]
    while stack:
        cur = stack.pop()
        if cur in visited: continue
        visited.add(cur)
        stack.extend(adj.get(cur, []))
"""


def count_components(adj: dict) -> int:
    visited: set = set()
    components = 0
    for node in adj:
        if node in visited:
            continue
        # DFS from node
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            stack.extend(adj.get(cur, []))
        components += 1
    return components
