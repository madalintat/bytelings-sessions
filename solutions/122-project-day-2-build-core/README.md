---
day: 122-project-day-2-build-core
phase: phase-5-algorithms
module: phase-5-project-pathfinder
style: build-it
---
# Day 122 — Day 2: fill in the three solvers

Yesterday's scaffold is ready. The parser works. `neighbors` yields
`(cell, cost)` pairs. Today you implement the three search algorithms.

All three return the same shape:

```python
tuple[list[Cell], int] | None
# (path_from_start_to_goal_inclusive, total_cost)
# OR None if no path exists.
```

Same return shape so the CLI tomorrow can swap them freely.

## BFS — shortest hop-count

You wrote BFS in Module 23. The only twist: track `parent` to
reconstruct the path. Use the same data:

```python
def solve_bfs(maze):
    start, goal = maze.start, maze.goal
    parent = {start: None}
    q = deque([start])
    while q:
        u = q.popleft()
        if u == goal:
            return _reconstruct(parent, start, goal)
        for v, _cost in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                q.append(v)
    return None
```

`_reconstruct` walks parent backward from goal. The cost is the path
*length minus 1* (number of edges).

## DFS — first-found path, not shortest

DFS is structurally the same, except a stack instead of a queue.
Crucially, **DFS doesn't give shortest paths**. It gives the first
path it stumbles onto — which depends on the neighbor order. That's
the lesson: same template, different guarantee.

```python
def solve_dfs(maze):
    start, goal = maze.start, maze.goal
    parent = {start: None}
    stack = [start]
    while stack:
        u = stack.pop()
        if u == goal:
            return _reconstruct(parent, start, goal)
        for v, _cost in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                stack.append(v)
    return None
```

(Recursive DFS works too — but on big mazes you'd hit Python's
recursion limit, so the iterative version is the safe default.)

## Dijkstra — shortest weighted path

Dijkstra generalizes BFS to *weighted* graphs with non-negative edge
costs. Instead of a queue (FIFO), use a min-heap keyed by current
known cost. Pop the cheapest-known cell next.

```python
import heapq

def solve_dijkstra(maze):
    start, goal = maze.start, maze.goal
    dist = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            return _reconstruct(parent, start, goal), d
        if d > dist[u]:
            continue                    # stale entry
        for v, w in neighbors(maze, u):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return None
```

The "stale entry" skip is the small detail that bites people. The
heap can hold *outdated* entries for cells you've found cheaper paths
to. When you pop one, just skip it.

## The path reconstruction helper

```python
def _reconstruct(parent, start, goal):
    if goal not in parent:
        return None
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path
```

Same helper for all three. Returns `[start, ..., goal]` inclusive.

## A subtle thing about BFS's "cost"

BFS returns hop count, but inside the search it doesn't track cost
explicitly. Compute it from path length:

```python
return path, len(path) - 1
```

That's only correct because BFS treats every edge as cost 1.
Dijkstra accumulates real `d` from the heap.

## Now: open `app.py`

Fill in the three solvers and `_reconstruct`. The tests will tell
you when each one passes.
