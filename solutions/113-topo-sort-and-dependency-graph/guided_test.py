"""Tests for rung 3."""
import importlib.util
import pytest
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _check(deps, order):
    pos = {n: i for i, n in enumerate(order)}
    for prereq, dependent in deps:
        assert pos[prereq] < pos[dependent]


def test_basic():
    deps = [("shared", "frontend"), ("shared", "backend")]
    order = ex.build_order(deps)
    _check(deps, order)
    assert set(order) == {"shared", "frontend", "backend"}


def test_chain():
    deps = [("a", "b"), ("b", "c"), ("c", "d")]
    assert ex.build_order(deps) == ["a", "b", "c", "d"]


def test_diamond():
    deps = [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d")]
    order = ex.build_order(deps)
    _check(deps, order)


def test_cycle_simple():
    with pytest.raises(ValueError):
        ex.build_order([("a", "b"), ("b", "a")])


def test_cycle_longer():
    with pytest.raises(ValueError):
        ex.build_order([("a", "b"), ("b", "c"), ("c", "a")])


def test_self_cycle():
    with pytest.raises(ValueError):
        ex.build_order([("a", "a")])


def test_empty():
    assert ex.build_order([]) == []
