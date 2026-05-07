---
day: day-111-bfs
phase: phase-5-algorithms
module: module-23-graphs
style: trace
---
# Day 111 — Trace BFS, level by level

Here's a tiny graph:

```text
       A
      / \
     B   C
    /|   |
   D E   F
       \  \
        G  H
```

Adjacency list:

```python
adj = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["H"],
    "G": [],
    "H": [],
}
```

You want to visit every node, **level by level**, starting from "A".
Predict what BFS visits first, second, third...

```python
from collections import deque

def bfs(adj, start):
    visited = {start}
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nb in adj[node]:
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
    return order
```

Trace by hand:

```text
q = [A]                     visit A → order = [A]
  A's neighbors: B, C       q = [B, C]
q = [B, C]                  visit B → order = [A, B]
  B's neighbors: D, E       q = [C, D, E]
q = [C, D, E]               visit C → order = [A, B, C]
  C's neighbors: F          q = [D, E, F]
... continues level by level: [A, B, C, D, E, F, G, H]
```

The output is exactly what you'd read off the picture going down,
left-to-right. That's the defining property of BFS: **visit all
distance-1 nodes before any distance-2 node.**

## Why the queue?

A queue is FIFO — first in, first out. Add neighbors to the back;
pull from the front. This guarantees you finish all of "today's"
neighbors before starting on "tomorrow's." Swap the queue for a
stack and BFS becomes DFS (next day).

## The two non-obvious details

**`visited` must be checked before pushing, not before visiting.**
If you check on `popleft` instead, you can push the same node many
times before it ever leaves the queue — quadratic blowup on dense
graphs.

**Don't mutate adj in the loop.** A common bug. If you "consume"
neighbors as you visit them, you can't run BFS twice on the same
graph.

## Shortest-path freebie

BFS doesn't just visit; it also tells you the *shortest path* from
start in unweighted graphs. Track each node's distance:

```python
dist = {start: 0}
q = deque([start])
while q:
    u = q.popleft()
    for nb in adj[u]:
        if nb not in dist:
            dist[nb] = dist[u] + 1
            q.append(nb)
```

After the loop, `dist[node]` is the fewest edges from `start`. Free.
This is why BFS is the right tool for:

- "Six degrees of Kevin Bacon" — shortest hop-count between two
  people.
- Maze solvers (PP5).
- Web crawlers that want to visit pages by link-distance.
- Any "what's the minimum number of steps to reach goal?" where steps
  are equal cost.

For *weighted* shortest paths, you upgrade BFS to Dijkstra. Same
shape; priority queue instead of plain queue.

## Now: open `02_fluency.py`

A BFS that pushes duplicates — the visited-set check is in the wrong
place. Fix it.
