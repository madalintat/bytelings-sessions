"""Tests for Day 2 — the three solvers."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SIMPLE = """\
S.G
"""

WALL = """\
S#G
"""

SQUARE = """\
S..
.#.
..G
"""

# A maze where Dijkstra should pick a longer hop-path because it costs less.
WEIGHTED = """\
S99G
.111
"""
# Going right (S, 9, 9, G) costs 9+9+1 = 19.
# Going down-around (S, ., 1, 1, 1, G) costs 1+1+1+1+1 = 5. Dijkstra wins.

UNREACHABLE = """\
S#
#G
"""


# ---- BFS -------------------------------------------------------------


def test_bfs_simple():
    m = ex.parse_maze(SIMPLE)
    path, cost = ex.solve_bfs(m)
    assert path[0] == (0, 0) and path[-1] == (0, 2)
    assert cost == 2


def test_bfs_square_shortest():
    m = ex.parse_maze(SQUARE)
    path, cost = ex.solve_bfs(m)
    assert cost == 4   # any 4-edge path through the corners


def test_bfs_unreachable():
    m = ex.parse_maze(UNREACHABLE)
    assert ex.solve_bfs(m) is None


def test_bfs_blocked():
    m = ex.parse_maze(WALL)
    assert ex.solve_bfs(m) is None


# ---- DFS -------------------------------------------------------------


def test_dfs_simple_finds_path():
    m = ex.parse_maze(SIMPLE)
    result = ex.solve_dfs(m)
    assert result is not None
    path, cost = result
    assert path[0] == (0, 0) and path[-1] == (0, 2)


def test_dfs_unreachable():
    m = ex.parse_maze(UNREACHABLE)
    assert ex.solve_dfs(m) is None


def test_dfs_finds_some_path_in_square():
    m = ex.parse_maze(SQUARE)
    result = ex.solve_dfs(m)
    assert result is not None
    path, _ = result
    assert path[0] == (0, 0) and path[-1] == (2, 2)


# ---- Dijkstra --------------------------------------------------------


def test_dijkstra_simple():
    m = ex.parse_maze(SIMPLE)
    path, cost = ex.solve_dijkstra(m)
    assert cost == 2   # two unit-cost edges


def test_dijkstra_prefers_cheaper_longer_path():
    m = ex.parse_maze(WEIGHTED)
    path, cost = ex.solve_dijkstra(m)
    # Cheapest is the bottom row: 5
    assert cost == 5


def test_dijkstra_unreachable():
    m = ex.parse_maze(UNREACHABLE)
    assert ex.solve_dijkstra(m) is None


def test_dijkstra_matches_bfs_on_unweighted():
    m = ex.parse_maze(SQUARE)
    bfs_cost = ex.solve_bfs(m)[1]
    dij_cost = ex.solve_dijkstra(m)[1]
    assert bfs_cost == dij_cost
