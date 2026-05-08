"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_simple_chain():
    adj = {1: [2], 2: [3], 3: []}
    assert ex.bfs_order(adj, 1) == [1, 2, 3]


def test_branching():
    adj = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [], "E": [], "F": [],
    }
    assert ex.bfs_order(adj, "A") == ["A", "B", "C", "D", "E", "F"]


def test_isolated_start():
    adj = {1: [], 2: [3]}
    assert ex.bfs_order(adj, 1) == [1]


def test_cycle():
    adj = {1: [2], 2: [3], 3: [1]}
    assert sorted(ex.bfs_order(adj, 1)) == [1, 2, 3]
    assert ex.bfs_order(adj, 1)[0] == 1


def test_diamond_no_dupes():
    """Both B and C point at D — D should appear exactly once."""
    adj = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    out = ex.bfs_order(adj, "A")
    assert sorted(out) == ["A", "B", "C", "D"]
    assert out.count("D") == 1
