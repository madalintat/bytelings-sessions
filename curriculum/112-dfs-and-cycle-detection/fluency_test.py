"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_acyclic():
    adj = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    assert ex.reachable(adj, "A") == {"A", "B", "C", "D"}


def test_cyclic_terminates():
    adj = {1: [2], 2: [3], 3: [1]}
    assert ex.reachable(adj, 1) == {1, 2, 3}


def test_isolated():
    adj = {1: [], 2: [3]}
    assert ex.reachable(adj, 1) == {1}


def test_self_loop():
    adj = {1: [1]}
    assert ex.reachable(adj, 1) == {1}


def test_disconnected_component_excluded():
    adj = {"A": ["B"], "B": [], "X": ["Y"], "Y": []}
    assert ex.reachable(adj, "A") == {"A", "B"}
