"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _normalize(adj):
    """Sort each neighbor list so order doesn't matter in tests."""
    return {k: sorted(v) for k, v in adj.items()}


def test_basic():
    adj = ex.build_undirected([("a", "b"), ("b", "c")])
    assert _normalize(adj) == {"a": ["b"], "b": ["a", "c"], "c": ["b"]}


def test_single_edge():
    adj = ex.build_undirected([(1, 2)])
    assert _normalize(adj) == {1: [2], 2: [1]}


def test_empty():
    assert ex.build_undirected([]) == {}


def test_triangle():
    adj = ex.build_undirected([(1, 2), (2, 3), (3, 1)])
    assert _normalize(adj) == {1: [2, 3], 2: [1, 3], 3: [1, 2]}
