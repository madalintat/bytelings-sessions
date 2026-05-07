"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_three_components():
    adj = {1: [2], 2: [1], 3: [4], 4: [3], 5: []}
    assert ex.count_components(adj) == 3


def test_empty():
    assert ex.count_components({}) == 0


def test_single_node():
    assert ex.count_components({1: []}) == 1


def test_one_big_component():
    adj = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
    assert ex.count_components(adj) == 1


def test_all_isolated():
    adj = {1: [], 2: [], 3: [], 4: []}
    assert ex.count_components(adj) == 4


def test_two_islands():
    adj = {
        "a": ["b", "c"], "b": ["a"], "c": ["a"],
        "x": ["y"], "y": ["x"],
    }
    assert ex.count_components(adj) == 2
