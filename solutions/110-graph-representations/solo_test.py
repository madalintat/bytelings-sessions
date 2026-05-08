"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_build_basic():
    out = ex.build_weighted([("a", "b", 5), ("a", "c", 2), ("b", "c", 1)])
    assert out == {"a": [("b", 5), ("c", 2)], "b": [("c", 1)]}


def test_build_empty():
    assert ex.build_weighted([]) == {}


def test_build_single():
    assert ex.build_weighted([(1, 2, 7)]) == {1: [(2, 7)]}


def test_total_weight_basic():
    adj = {"a": [("b", 5), ("c", 2)], "b": [("c", 1)]}
    assert ex.total_weight(adj) == 8


def test_total_weight_empty():
    assert ex.total_weight({}) == 0


def test_total_weight_with_isolated():
    adj = {"a": [], "b": [("c", 3)]}
    assert ex.total_weight(adj) == 3


def test_round_trip():
    edges = [("a", "b", 1), ("a", "c", 2), ("c", "d", 3)]
    adj = ex.build_weighted(edges)
    assert ex.total_weight(adj) == 6
