"""Tests for rung 3."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_open_3x3():
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    result = ex.count_paths(grid)
    diagnose(
        result == 6,
        f"Open 3x3 grid has 6 paths (C(4,2)); got {result}.",
        (lambda: result == 1,
         "You returned 1 — looks like only one path was explored."
         " Make sure you add both count(i+1,j) and count(i,j+1)."),
        (lambda: result == 0,
         "You returned 0 — base case or bounds check is too restrictive."
         " The bottom-right cell should return 1, not 0."),
    )


def test_blocked_center():
    grid = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    result = ex.count_paths(grid)
    diagnose(
        result == 2,
        f"Center-blocked 3x3 has 2 paths; got {result}.",
        (lambda: result == 6,
         "You got 6 — you're not respecting the blocked cell (value 1)."
         " Return 0 whenever grid[i][j] == 1."),
    )


def test_blocked_path():
    grid = [[0, 1],
            [1, 0]]
    assert ex.count_paths(grid) == 0


def test_single_cell():
    assert ex.count_paths([[0]]) == 1


def test_single_row():
    assert ex.count_paths([[0, 0, 0, 0]]) == 1


def test_single_col():
    assert ex.count_paths([[0], [0], [0]]) == 1


def test_start_blocked():
    assert ex.count_paths([[1, 0], [0, 0]]) == 0


def test_end_blocked():
    assert ex.count_paths([[0, 0], [0, 1]]) == 0
