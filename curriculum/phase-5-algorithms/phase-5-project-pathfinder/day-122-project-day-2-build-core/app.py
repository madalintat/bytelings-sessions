"""Pathfinder — Day 2.

Today: implement BFS, DFS, Dijkstra. Each returns
  tuple[list[Cell], int] | None
where the path includes both S and G, and the int is the cost.

The parser and neighbors function from Day 1 are pre-filled below.
"""
from collections import deque
from dataclasses import dataclass
import heapq
from typing import Iterator


Cell = tuple[int, int]
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


@dataclass
class Maze:
    grid: list[list[str]]
    start: Cell
    goal: Cell
    rows: int
    cols: int


def parse_maze(text: str) -> Maze:
    lines = [line for line in text.splitlines() if line]
    rows = len(lines)
    cols = max(len(line) for line in lines) if lines else 0
    grid = [list(line.ljust(cols, "#")) for line in lines]
    start = goal = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            elif ch == "G":
                goal = (r, c)
    if start is None:
        raise ValueError("maze missing start 'S'")
    if goal is None:
        raise ValueError("maze missing goal 'G'")
    return Maze(grid=grid, start=start, goal=goal, rows=rows, cols=cols)


def neighbors(maze: Maze, cell: Cell) -> Iterator[tuple[Cell, int]]:
    r, c = cell
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < maze.rows and 0 <= nc < maze.cols):
            continue
        ch = maze.grid[nr][nc]
        if ch == "#":
            continue
        cost = int(ch) if ch.isdigit() else 1
        yield (nr, nc), cost


def _reconstruct(parent: dict, start: Cell, goal: Cell) -> list[Cell] | None:
    """Walk parent from goal back to start; return [start, ..., goal]."""
    # TODO: implement
    raise NotImplementedError


def solve_bfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """Return (path, hop_count) using BFS — shortest by hop count."""
    # TODO: implement using deque + parent dict
    raise NotImplementedError


def solve_dfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """Return (path, hop_count) using iterative DFS.

    Note: DFS does NOT promise shortest. The path it returns depends on
    neighbor traversal order.
    """
    # TODO: implement using stack (list) + parent dict
    raise NotImplementedError


def solve_dijkstra(maze: Maze) -> tuple[list[Cell], int] | None:
    """Return (path, total_weighted_cost) using Dijkstra's algorithm."""
    # TODO: implement using heapq + dist dict + parent dict
    raise NotImplementedError
