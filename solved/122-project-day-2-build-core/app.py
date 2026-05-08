"""Day 122 — Pathfinder Day 2: three solvers.

All three solvers return (path, cost) | None.
'path' is [start, ..., goal] inclusive.

BFS: shortest hop-count via deque + parent dict.
DFS: first-found path via stack + parent dict.  Does NOT guarantee shortest.
Dijkstra: shortest weighted path via min-heap.  The "stale entry" guard
    (`if d > dist[u]: continue`) prevents re-processing cheaper-path cells.

The `_reconstruct` helper is shared; it walks the parent chain backward.

Cost note: BFS uses `len(path) - 1` because every edge costs 1 in BFS's model.
Dijkstra accumulates real weighted costs from the heap.
"""
from __future__ import annotations

import heapq
from collections import deque
from dataclasses import dataclass
from typing import Iterator

# ---------------------------------------------------------------------------
# Types (identical to Day 121)
# ---------------------------------------------------------------------------

Cell = tuple[int, int]
DIRS: tuple[tuple[int, int], ...] = ((-1, 0), (1, 0), (0, -1), (0, 1))


@dataclass
class Maze:
    grid: list[list[str]]
    start: Cell
    goal: Cell
    rows: int
    cols: int


# ---------------------------------------------------------------------------
# Parser + neighbors (carried forward from Day 121)
# ---------------------------------------------------------------------------

def parse_maze(text: str) -> Maze:
    """Parse an ASCII maze string into a Maze dataclass."""
    grid: list[list[str]] = []
    start: Cell = (0, 0)
    goal: Cell = (0, 0)
    for r, line in enumerate(text.splitlines()):
        if not line:
            continue
        row = list(line)
        grid.append(row)
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            elif ch == "G":
                goal = (r, c)
    rows = len(grid)
    cols = max(len(row) for row in grid) if grid else 0
    return Maze(grid=grid, start=start, goal=goal, rows=rows, cols=cols)


def neighbors(maze: Maze, cell: Cell) -> Iterator[tuple[Cell, int]]:
    """Yield (neighbor_cell, edge_cost) for each walkable neighbour."""
    r, c = cell
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < maze.rows and 0 <= nc < maze.cols:
            ch = maze.grid[nr][nc]
            if ch == "#":
                continue
            cost = int(ch) if ch.isdigit() else 1
            yield (nr, nc), cost


# ---------------------------------------------------------------------------
# Shared path-reconstruction helper
# ---------------------------------------------------------------------------

def _reconstruct(
    parent: dict[Cell, Cell | None], start: Cell, goal: Cell
) -> list[Cell] | None:
    """Walk the parent dict from goal back to start; return reversed path."""
    if goal not in parent:
        return None
    path: list[Cell] = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])  # type: ignore[arg-type]
    path.reverse()
    return path


# ---------------------------------------------------------------------------
# Solvers
# ---------------------------------------------------------------------------

def solve_bfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """BFS — shortest hop-count path."""
    start, goal = maze.start, maze.goal
    parent: dict[Cell, Cell | None] = {start: None}
    q: deque[Cell] = deque([start])
    while q:
        u = q.popleft()
        if u == goal:
            path = _reconstruct(parent, start, goal)
            if path is None:
                return None
            return path, len(path) - 1
        for v, _cost in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                q.append(v)
    return None


def solve_dfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """DFS — first-found path (not necessarily shortest)."""
    start, goal = maze.start, maze.goal
    parent: dict[Cell, Cell | None] = {start: None}
    stack: list[Cell] = [start]
    while stack:
        u = stack.pop()
        if u == goal:
            path = _reconstruct(parent, start, goal)
            if path is None:
                return None
            return path, len(path) - 1
        for v, _cost in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                stack.append(v)
    return None


def solve_dijkstra(maze: Maze) -> tuple[list[Cell], int] | None:
    """Dijkstra — shortest weighted path."""
    start, goal = maze.start, maze.goal
    dist: dict[Cell, int] = {start: 0}
    parent: dict[Cell, Cell | None] = {start: None}
    pq: list[tuple[int, Cell]] = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            path = _reconstruct(parent, start, goal)
            if path is None:
                return None
            return path, d
        if d > dist[u]:
            continue  # stale heap entry
        for v, w in neighbors(maze, u):
            nd = d + w
            if nd < dist.get(v, 10**9):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return None
