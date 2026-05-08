"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _is_valid_path(adj, path, start, goal):
    if path[0] != start or path[-1] != goal:
        return False
    for a, b in zip(path, path[1:]):
        if b not in adj.get(a, []):
            return False
    return True


def test_basic():
    adj = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}
    p = ex.shortest_path(adj, "A", "E")
    assert _is_valid_path(adj, p, "A", "E")
    assert len(p) == 4   # A -> {B|C} -> D -> E


def test_self():
    adj = {1: [2]}
    assert ex.shortest_path(adj, 1, 1) == [1]


def test_unreachable():
    adj = {1: [2], 2: [], 9: []}
    assert ex.shortest_path(adj, 1, 9) is None


def test_direct():
    adj = {1: [2]}
    assert ex.shortest_path(adj, 1, 2) == [1, 2]


def test_chain():
    adj = {1: [2], 2: [3], 3: [4], 4: []}
    assert ex.shortest_path(adj, 1, 4) == [1, 2, 3, 4]


def test_picks_shortest_when_two_options():
    adj = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "E": ["D"], "D": []}
    p = ex.shortest_path(adj, "A", "D")
    assert len(p) == 3
    assert _is_valid_path(adj, p, "A", "D")
