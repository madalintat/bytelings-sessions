---
day: day-112-dfs-and-cycle-detection
phase: phase-5-algorithms
module: module-23-graphs
style: build-it
---
# Day 112 — Build DFS, then catch a cycle with it

DFS — depth-first search — is BFS's older sibling. Same job (visit
every reachable node), opposite strategy.

- BFS: queue, level by level, breadth first.
- DFS: stack (or recursion), go deep before going wide.

Pretend Python doesn't ship a graph library. Build it.

## Recursive DFS

```python
def dfs(adj, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nb in adj.get(start, []):
        if nb not in visited:
            dfs(adj, nb, visited)
    return visited
```

That's the whole thing. The recursion gives you the stack for free.
Trace `dfs(adj, A)` on the same tree from yesterday: A, B, D, then
back up, E, G, back up, then C, F, H. The order zig-zags down, then
sideways — depth first.

## Iterative DFS (when recursion would blow the stack)

```python
def dfs_iter(adj, start):
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for nb in adj.get(node, []):
            if nb not in visited:
                visited.add(nb)
                stack.append(nb)
    return visited
```

Note the only difference from BFS: `stack.pop()` (LIFO) instead of
`q.popleft()` (FIFO). One swap turns BFS into DFS. Same template.

## DFS lets you catch cycles

A graph has a cycle if, while exploring from a node, you find an edge
back to a node *already on the current recursion path*. There are
three states each node can be in during DFS:

- **WHITE** — not yet visited.
- **GRAY** — currently being explored (on the recursion stack).
- **BLACK** — fully explored (DFS returned for this node).

A cycle exists if you ever traverse an edge from a GRAY node to
another GRAY node — that's the back-edge. Going GRAY → WHITE means
you're descending; GRAY → BLACK means you found a node that was
already done (no cycle, just a shortcut).

```python
def has_cycle(adj):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in adj}

    def visit(u):
        color[u] = GRAY
        for v in adj[u]:
            if color.get(v, WHITE) == GRAY:
                return True               # back-edge → cycle
            if color.get(v, WHITE) == WHITE and visit(v):
                return True
        color[u] = BLACK
        return False

    return any(visit(u) for u in adj if color[u] == WHITE)
```

For **undirected** graphs, the rule changes slightly — you have to
ignore the edge you just came from, otherwise every edge looks like
a cycle. We'll keep things directed today.

## WHEN to reach for DFS

DFS is the right tool whenever:

- **You need to visit every node** but don't care about levels (just
  reachability or component-counting).
- **You're looking for cycles** (above) — directly the GRAY-detect
  pattern.
- **You're doing a topological sort** (tomorrow) — DFS, finishing
  order, reverse it.
- **The structure is a tree and you want pre/in/post-order traversal.**
- **Backtracking** (Module 24) — DFS is backtracking's bones.

You'll see DFS in every compiler (cycle detection in dependencies),
every package manager (resolve install order with topo sort), every
build system (rebuild graph), and every linter that checks for
import cycles.

## Now: open `fluency.py`

A DFS that infinite-loops on cyclic graphs. Add the visited check.
