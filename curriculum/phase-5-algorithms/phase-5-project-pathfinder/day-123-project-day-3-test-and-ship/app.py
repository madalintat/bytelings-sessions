"""Pathfinder — Day 3.

Today: rendering, the run_cli wrapper, and a small argparse main.
The parser and three solvers are filled in below from earlier days.
"""
import argparse
import heapq
import sys
from collections import deque
from dataclasses import dataclass
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
    if goal not in parent:
        return None
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def solve_bfs(maze: Maze) -> tuple[list[Cell], int] | None:
    start, goal = maze.start, maze.goal
    if start == goal:
        return [start], 0
    parent = {start: None}
    q = deque([start])
    while q:
        u = q.popleft()
        if u == goal:
            path = _reconstruct(parent, start, goal)
            return path, len(path) - 1
        for v, _w in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                q.append(v)
    return None


def solve_dfs(maze: Maze) -> tuple[list[Cell], int] | None:
    start, goal = maze.start, maze.goal
    if start == goal:
        return [start], 0
    parent = {start: None}
    stack = [start]
    while stack:
        u = stack.pop()
        if u == goal:
            path = _reconstruct(parent, start, goal)
            return path, len(path) - 1
        for v, _w in neighbors(maze, u):
            if v not in parent:
                parent[v] = u
                stack.append(v)
    return None


def solve_dijkstra(maze: Maze) -> tuple[list[Cell], int] | None:
    start, goal = maze.start, maze.goal
    dist = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            path = _reconstruct(parent, start, goal)
            return path, d
        if d > dist[u]:
            continue
        for v, w in neighbors(maze, u):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return None


def render_path(maze: Maze, path: list[Cell]) -> str:
    """Overlay path on the grid using '*'. Keep S and G visible."""
    # TODO: implement
    raise NotImplementedError


def run_cli(algo: str, maze_text: str) -> tuple[str, str]:
    """Solve and render. Returns (grid_text, status_line).

    Unknown algo → ('', 'unknown algorithm: ...').
    No path     → (original_grid_text, 'no path found').
    Found path  → (rendered_grid, f'path found, cost={cost}, length={len}').
    """
    # TODO: implement
    raise NotImplementedError


def main() -> None:
    p = argparse.ArgumentParser(description="Maze pathfinder.")
    p.add_argument("--algo", default="bfs", choices=("bfs", "dfs", "dijkstra"))
    p.add_argument("file", nargs="?", default="-",
                   help="maze file path, or '-' for stdin")
    args = p.parse_args()
    text = sys.stdin.read() if args.file == "-" else open(args.file).read()
    rendered, status = run_cli(args.algo, text)
    if rendered:
        print(rendered)
    print(status)


if __name__ == "__main__":
    main()
