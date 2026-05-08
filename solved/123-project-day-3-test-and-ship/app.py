"""Day 123 — Pathfinder Day 3: render + CLI.

render_path: deep-copies the grid, overlays '*' on every path cell
    except S and G, then joins rows into a multi-line string.

run_cli: a pure function (maze_text + algo name → rendered grid, status),
    making it straightforwardly testable.  The argparse main() layer
    wraps it for interactive use.

Return shapes:
    render_path  -> str
    run_cli      -> tuple[str, str]   (grid_text, status_line)
"""
from __future__ import annotations

import argparse
import heapq
import sys
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
# Parser + neighbors
# ---------------------------------------------------------------------------

def parse_maze(text: str) -> Maze:
    """Parse ASCII maze into a Maze dataclass."""
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
    """Yield (neighbor_cell, edge_cost) for walkable neighbours."""
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
# Path reconstruction
# ---------------------------------------------------------------------------

def _reconstruct(
    parent: dict[Cell, Cell | None], start: Cell, goal: Cell
) -> list[Cell] | None:
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
    start, goal = maze.start, maze.goal
    parent: dict[Cell, Cell | None] = {start: None}
    q: deque[Cell] = deque([start])
    while q:
        u = q.popleft()
        if u == goal:
            path = _reconstruct(parent, start, goal)
            return (path, len(path) - 1) if path else None
        for v, _ in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                q.append(v)
    return None


def solve_dfs(maze: Maze) -> tuple[list[Cell], int] | None:
    start, goal = maze.start, maze.goal
    parent: dict[Cell, Cell | None] = {start: None}
    stack: list[Cell] = [start]
    while stack:
        u = stack.pop()
        if u == goal:
            path = _reconstruct(parent, start, goal)
            return (path, len(path) - 1) if path else None
        for v, _ in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                stack.append(v)
    return None


def solve_dijkstra(maze: Maze) -> tuple[list[Cell], int] | None:
    start, goal = maze.start, maze.goal
    dist: dict[Cell, int] = {start: 0}
    parent: dict[Cell, Cell | None] = {start: None}
    pq: list[tuple[int, Cell]] = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            path = _reconstruct(parent, start, goal)
            return (path, d) if path else None
        if d > dist[u]:
            continue
        for v, w in neighbors(maze, u):
            nd = d + w
            if nd < dist.get(v, 10**9):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return None


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def render_path(maze: Maze, path: list[Cell]) -> str:
    """Return the maze grid with '*' overlaid on every path step except S/G."""
    grid = [row[:] for row in maze.grid]
    for r, c in path:
        if grid[r][c] not in ("S", "G"):
            grid[r][c] = "*"
    return "\n".join("".join(row) for row in grid)


# ---------------------------------------------------------------------------
# CLI helper (testable)
# ---------------------------------------------------------------------------

_SOLVERS = {"bfs": solve_bfs, "dfs": solve_dfs, "dijkstra": solve_dijkstra}


def run_cli(algo: str, maze_text: str) -> tuple[str, str]:
    """Run *algo* on *maze_text* and return (rendered_grid, status_line).

    Status: 'path found, cost=<n>, length=<k>'  or  'no path found'.
    Returns ('', 'unknown algorithm: <algo>') for an unrecognised algo name.
    """
    if algo not in _SOLVERS:
        return ("", f"unknown algorithm: {algo}")
    maze = parse_maze(maze_text)
    result = _SOLVERS[algo](maze)
    if result is None:
        return (maze_text.rstrip(), "no path found")
    path, cost = result
    rendered = render_path(maze, path)
    return (rendered, f"path found, cost={cost}, length={len(path)}")


# ---------------------------------------------------------------------------
# Argparse entry point
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(description="ASCII maze solver")
    p.add_argument("--algo", default="bfs", choices=("bfs", "dfs", "dijkstra"))
    p.add_argument("file", nargs="?", default="-", help="maze file or '-' for stdin")
    args = p.parse_args()
    text = sys.stdin.read() if args.file == "-" else open(args.file).read()
    rendered, status = run_cli(args.algo, text)
    print(rendered)
    print(status)


if __name__ == "__main__":
    main()
