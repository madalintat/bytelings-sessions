"""Day 121 — Pathfinder Day 1: parser, neighbors, stubs.

Design choices:
- Cell is tuple[int, int] (row, col): hashable, immutable, cheap to copy.
- Maze is a dataclass holding the parsed grid plus pre-computed start/goal/dims.
- `neighbors` centralises edge-cost logic so all three solvers share it;
  digits '1'–'9' carry their face value, walkable non-digit cells cost 1.
- DIRS order is deterministic (up/down/left/right), which keeps test paths stable.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterator

# ---------------------------------------------------------------------------
# Types
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
# Parser
# ---------------------------------------------------------------------------

def parse_maze(text: str) -> Maze:
    """Parse an ASCII maze string into a Maze dataclass.

    'S' marks the start, 'G' marks the goal.  '#' is a wall.
    Digits '1'–'9' are passable cells with that movement cost.
    '.' is a passable cell with cost 1.

    >>> m = parse_maze("S.G")
    >>> m.start, m.goal
    ((0, 0), (0, 2))
    """
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


# ---------------------------------------------------------------------------
# Neighbor function (shared by all three solvers)
# ---------------------------------------------------------------------------

def neighbors(maze: Maze, cell: Cell) -> Iterator[tuple[Cell, int]]:
    """Yield (neighbor_cell, edge_cost) for each walkable neighbour of cell.

    Walls ('#') are silently skipped.  Digit cells '1'–'9' yield their
    numeric cost; all other walkable characters yield cost 1.
    """
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
# Solver stubs (filled in Day 122)
# ---------------------------------------------------------------------------

def solve_bfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """BFS — shortest hop-count path.  Implemented on Day 122."""
    raise NotImplementedError


def solve_dfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """DFS — first-found path.  Implemented on Day 122."""
    raise NotImplementedError


def solve_dijkstra(maze: Maze) -> tuple[list[Cell], int] | None:
    """Dijkstra — shortest weighted path.  Implemented on Day 122."""
    raise NotImplementedError
