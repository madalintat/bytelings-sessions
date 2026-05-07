"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_acyclic_chain():
    assert ex.has_cycle({1: [2], 2: [3], 3: []}) is False


def test_simple_cycle():
    assert ex.has_cycle({1: [2], 2: [3], 3: [1]}) is True


def test_self_loop():
    assert ex.has_cycle({1: [1]}) is True


def test_dag():
    adj = {1: [2, 3], 2: [4], 3: [4], 4: []}
    assert ex.has_cycle(adj) is False


def test_cycle_in_one_component():
    adj = {1: [2], 2: [3], 3: [], 10: [11], 11: [10]}
    assert ex.has_cycle(adj) is True


def test_empty():
    assert ex.has_cycle({}) is False


def test_single_node_no_edge():
    assert ex.has_cycle({1: []}) is False


def test_long_acyclic():
    adj = {i: [i + 1] for i in range(100)}
    adj[100] = []
    assert ex.has_cycle(adj) is False


def test_back_edge_deep():
    adj = {1: [2], 2: [3], 3: [4], 4: [5], 5: [2]}
    assert ex.has_cycle(adj) is True
