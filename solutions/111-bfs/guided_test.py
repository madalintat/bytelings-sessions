"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    adj = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert ex.shortest_distances(adj, "A") == {"A": 0, "B": 1, "C": 1, "D": 2}


def test_unreachable_excluded():
    adj = {"A": ["B"], "B": [], "X": ["Y"], "Y": []}
    assert ex.shortest_distances(adj, "A") == {"A": 0, "B": 1}


def test_chain():
    adj = {1: [2], 2: [3], 3: [4], 4: []}
    assert ex.shortest_distances(adj, 1) == {1: 0, 2: 1, 3: 2, 4: 3}


def test_self_only():
    adj = {1: []}
    assert ex.shortest_distances(adj, 1) == {1: 0}


def test_cycle():
    adj = {1: [2], 2: [3], 3: [1]}
    assert ex.shortest_distances(adj, 1) == {1: 0, 2: 1, 3: 2}


def test_pick_shortest_via_other_path():
    """Shortest path to D goes via B, not via the longer A->C->E->D."""
    adj = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "E": ["D"], "D": []}
    assert ex.shortest_distances(adj, "A")["D"] == 2
