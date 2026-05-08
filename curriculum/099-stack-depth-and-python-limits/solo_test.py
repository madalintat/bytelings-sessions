"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def leaf(v):
    return {"value": v, "children": []}


def test_single():
    assert ex.max_value(leaf(5)) == 5


def test_root_max():
    n = {"value": 100, "children": [leaf(1), leaf(2)]}
    assert ex.max_value(n) == 100


def test_child_max():
    n = {"value": 1, "children": [leaf(50), leaf(2)]}
    assert ex.max_value(n) == 50


def test_negative():
    n = {"value": -3, "children": [leaf(-1), leaf(-7)]}
    assert ex.max_value(n) == -1


def test_nested():
    inner = {"value": 4, "children": [leaf(99)]}
    outer = {"value": 1, "children": [inner, leaf(2)]}
    assert ex.max_value(outer) == 99


def test_very_deep_no_recursion_error():
    cur = leaf(1)
    for i in range(2000):
        cur = {"value": i, "children": [cur]}
    assert ex.max_value(cur) == 1999
