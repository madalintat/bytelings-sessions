"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _is_valid(adj, order):
    pos = {n: i for i, n in enumerate(order)}
    for u in adj:
        for v in adj[u]:
            if pos.get(u, -1) >= pos.get(v, -1):
                return False
    return True


def test_basic():
    adj = {"shared-utils": ["frontend"], "frontend": []}
    order = ex.topo_sort(adj)
    assert _is_valid(adj, order)
    assert set(order) == {"shared-utils", "frontend"}


def test_diamond():
    adj = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}
    order = ex.topo_sort(adj)
    assert _is_valid(adj, order)
    assert len(order) == 4


def test_chain():
    adj = {1: [2], 2: [3], 3: [4], 4: []}
    assert ex.topo_sort(adj) == [1, 2, 3, 4]


def test_isolated_node():
    adj = {1: [2], 2: [], 99: []}
    order = ex.topo_sort(adj)
    assert set(order) == {1, 2, 99}
    assert _is_valid(adj, order)


def test_empty():
    assert ex.topo_sort({}) == []
