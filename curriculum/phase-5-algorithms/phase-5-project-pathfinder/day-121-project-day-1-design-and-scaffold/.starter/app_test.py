"""Tests for Day 1 — parser + neighbors function.

Solver tests are HIDDEN at the bottom but expected to fail today.
"""
import importlib.util
import pytest
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SIMPLE = """\
S.G
"""

BLOCKED = """\
S#G
"""

WEIGHTED = """\
S2.G
"""

SQUARE = """\
S..
.#.
..G
"""


# ---- parse_maze ------------------------------------------------------


def test_parse_basic():
    m = ex.parse_maze(SIMPLE)
    assert m.start == (0, 0)
    assert m.goal == (0, 2)
    assert m.rows == 1
    assert m.cols == 3


def test_parse_square():
    m = ex.parse_maze(SQUARE)
    assert m.start == (0, 0)
    assert m.goal == (2, 2)
    assert m.rows == 3
    assert m.cols == 3
    assert m.grid[1][1] == "#"


def test_parse_missing_start():
    with pytest.raises(ValueError):
        ex.parse_maze("...G")


def test_parse_missing_goal():
    with pytest.raises(ValueError):
        ex.parse_maze("S...")


# ---- neighbors -------------------------------------------------------


def test_neighbors_open():
    m = ex.parse_maze(SIMPLE)
    out = list(ex.neighbors(m, (0, 0)))
    # S at (0,0); right-neighbor (0,1) is '.', cost 1.
    assert ((0, 1), 1) in out


def test_neighbors_skip_walls():
    m = ex.parse_maze(BLOCKED)
    out = list(ex.neighbors(m, (0, 0)))
    # Wall to the right; no neighbors.
    cells = [c for c, _ in out]
    assert (0, 1) not in cells


def test_neighbors_weighted():
    m = ex.parse_maze(WEIGHTED)
    # S(0,0) right-neighbor is '2' (cost 2)
    out = dict(ex.neighbors(m, (0, 0)))
    assert out.get((0, 1)) == 2


def test_neighbors_corner_only_two():
    m = ex.parse_maze(SQUARE)
    out = list(ex.neighbors(m, (0, 0)))
    cells = {c for c, _ in out}
    assert cells == {(0, 1), (1, 0)}


def test_neighbors_skips_out_of_bounds():
    m = ex.parse_maze(SQUARE)
    out = list(ex.neighbors(m, (0, 2)))
    cells = {c for c, _ in out}
    # (0,2)'s neighbors: (0,1) '.' yes; (1,2) '.' yes; up/right OOB.
    assert cells == {(0, 1), (1, 2)}


# ---- solver stubs should at least raise NotImplementedError ----------


def test_solve_stubs_exist():
    m = ex.parse_maze(SIMPLE)
    for fn in (ex.solve_bfs, ex.solve_dfs, ex.solve_dijkstra):
        with pytest.raises(NotImplementedError):
            fn(m)
