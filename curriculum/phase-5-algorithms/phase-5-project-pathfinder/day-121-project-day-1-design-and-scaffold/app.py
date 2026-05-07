"""Pathfinder — Day 1.

Today: build the maze parser, the neighbor function, and stub the
three solvers. Tomorrow you fill in the solver bodies.
"""
from dataclasses import dataclass
from typing import Iterator


Cell = tuple[int, int]
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))   # up, down, left, right


@dataclass
class Maze:
    grid: list[list[str]]
    start: Cell
    goal: Cell
    rows: int
    cols: int


def parse_maze(text: str) -> Maze:
    """Parse an ASCII maze into a Maze object.

    Characters:
      - 'S' start (exactly one)
      - 'G' goal  (exactly one)
      - '#' wall (impassable)
      - '.' open floor (cost 1)
      - '1'..'9' open floor with that movement cost
    Trailing newlines are ignored. Raises ValueError if S or G is missing.
    """
    # TODO: implement
    raise NotImplementedError


def neighbors(maze: Maze, cell: Cell) -> Iterator[tuple[Cell, int]]:
    """Yield (neighbor, edge_cost) for each open cell adjacent to `cell`.

    Walls ('#') are skipped. Cost rules:
      - '.', 'S', 'G' → cost 1
      - '1'..'9'      → cost equal to the digit

    Out-of-bounds neighbors are skipped silently.
    """
    # TODO: implement
    raise NotImplementedError


# ---- Solver stubs (Day 122 fills these in) ---------------------------


def solve_bfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """Return (path_including_S_and_G, hop_count) or None."""
    raise NotImplementedError


def solve_dfs(maze: Maze) -> tuple[list[Cell], int] | None:
    """Return (path_including_S_and_G, hop_count) or None.

    DFS does NOT promise shortest. Returns the first path it finds.
    """
    raise NotImplementedError


def solve_dijkstra(maze: Maze) -> tuple[list[Cell], int] | None:
    """Return (path_including_S_and_G, total_weighted_cost) or None."""
    raise NotImplementedError
