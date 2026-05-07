"""Tests for Day 3 — render_path, run_cli, and edge cases."""
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

SQUARE = """\
S..
.#.
..G
"""

START_EQ_GOAL = "S"   # a one-cell maze where S == G is impossible (only 1 letter)
# Actually we can test S==G by overlapping start and goal positions —
# but a single cell can only be one letter. So we'll test the "adjacent"
# case as a stand-in for the trivial path.

ADJACENT = """\
SG
"""

WEIGHTED = """\
S99G
.111
"""

NO_PATH = """\
S#
#G
"""


# ---- render_path -----------------------------------------------------


def test_render_simple():
    m = ex.parse_maze(SIMPLE)
    path = [(0, 0), (0, 1), (0, 2)]
    out = ex.render_path(m, path)
    assert out == "S*G"


def test_render_does_not_overwrite_S_or_G():
    m = ex.parse_maze(SIMPLE)
    path = [(0, 0), (0, 1), (0, 2)]
    out = ex.render_path(m, path)
    assert "S" in out and "G" in out


def test_render_multiline_square():
    m = ex.parse_maze(SQUARE)
    path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    out = ex.render_path(m, path)
    lines = out.splitlines()
    assert lines[0] == "S**"
    assert lines[2].endswith("*G")


# ---- run_cli ---------------------------------------------------------


def test_run_cli_bfs_found():
    rendered, status = ex.run_cli("bfs", SIMPLE)
    assert "path found" in status
    assert "cost=2" in status


def test_run_cli_no_path():
    rendered, status = ex.run_cli("bfs", NO_PATH)
    assert status == "no path found"


def test_run_cli_unknown_algo():
    _, status = ex.run_cli("astar", SIMPLE)
    assert "unknown algorithm" in status


def test_run_cli_dijkstra_picks_cheap_path():
    _, status = ex.run_cli("dijkstra", WEIGHTED)
    assert "cost=5" in status   # the long-but-cheap bottom row


def test_run_cli_bfs_picks_short_path():
    _, status = ex.run_cli("bfs", WEIGHTED)
    # BFS counts hops, ignores weights. Top row is 3 hops.
    assert "cost=3" in status


# ---- edge cases ------------------------------------------------------


def test_adjacent_start_goal_bfs():
    m = ex.parse_maze(ADJACENT)
    path, cost = ex.solve_bfs(m)
    assert path == [(0, 0), (0, 1)]
    assert cost == 1


def test_adjacent_start_goal_dijkstra():
    m = ex.parse_maze(ADJACENT)
    path, cost = ex.solve_dijkstra(m)
    assert cost == 1


def test_render_only_marks_path_cells():
    m = ex.parse_maze(SQUARE)
    path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    out = ex.render_path(m, path)
    # The wall at (1,1) and the unused (0,1), (0,2), (1,2) should NOT
    # become '*'. Count stars: should equal len(path) - 2 (S and G excluded).
    assert out.count("*") == len(path) - 2
