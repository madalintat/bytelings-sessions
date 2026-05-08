---
day: day-113-topo-sort-and-dependency-graph
phase: phase-5-algorithms
module: module-23-graphs
style: story
---
# Day 113 — The morning the build failed in alphabetical order

You're on call. At 03:14 the build pipeline crashes. The error log
helpfully reads:

```text
ERROR: cannot build 'frontend' — dependency 'shared-utils' was not built first
```

You investigate. Yesterday someone refactored the build runner. Now
it builds packages **alphabetically**. `frontend` starts with F.
`shared-utils` starts with S. F runs first. F needs S. F crashes.

The fix isn't to rename packages. The fix is to build them in **topo
order**.

## What's a topological sort?

A topological sort of a directed acyclic graph (DAG) is a linear
ordering of nodes such that for every edge `u → v`, `u` comes before
`v`. In dependency-graph terms: "build the leaves first, then their
parents, never the other way."

Multiple valid topo orders usually exist for the same DAG — your
algorithm just needs to produce *one* of them. Which one depends on
which choices you make at ties.

A graph has a topo order **if and only if it has no cycles**. A
cycle means "A depends on B which depends on A" — there's no way to
build either first. (Yesterday's `has_cycle` is your sanity check.)

## Kahn's algorithm — the build-runner-friendly one

Compute in-degree (count of incoming edges) for every node.
Repeatedly:
1. Pick any node with in-degree 0 (no remaining prerequisites).
2. Add it to the output. Remove it from the graph (decrement in-degree
   of its neighbors).
3. Stop when all nodes are emitted, OR when no in-degree-0 node
   exists with nodes remaining (that's a cycle — error out).

```python
from collections import deque, defaultdict

def topo(adj):
    indeg = defaultdict(int)
    for u in adj:
        indeg.setdefault(u, 0)
        for v in adj[u]:
            indeg[v] += 1
    q = deque(n for n, d in indeg.items() if d == 0)
    out = []
    while q:
        u = q.popleft()
        out.append(u)
        for v in adj.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(out) != len(indeg):
        raise ValueError("graph has a cycle")
    return out
```

The `q` here can be a deque, a heap (for "always pick the smallest"),
or a list — choice affects which valid topo order you get, but all
are valid.

## DFS-based topo sort — the alternative

Run DFS, record each node's *finish time* (when DFS returns from it),
then output nodes in reverse finish order. Same answer, different
shape. Useful when you're already running DFS for cycle detection;
you get topo for free.

## WHEN you actually need topo sort

The story is the punch line: anything with **dependencies that have
to happen in the right order**.

- **Build systems.** make, ninja, cargo, sbt, gradle. All resolve
  build order via topo sort.
- **Package managers.** pip, npm, apt. Install dependencies before
  dependents.
- **Course scheduling.** Take prerequisites before dependents.
- **Spreadsheet recalculation.** Cell B depends on A; recompute A
  first.
- **Database migration runners.** Apply earlier migrations before
  later ones, with explicit `depends_on` lists.
- **Task runners (Airflow, Dagster).** DAG = directed acyclic graph
  *literally* in the name.

If you're writing a system where "X must happen before Y," you need
topo sort. Don't invent your own ordering — implement it once,
correctly, with a cycle check.

## Now: open `fluency.py`

A topo-sort that emits nodes too eagerly — it doesn't decrement
in-degree on neighbors. Fix it.
