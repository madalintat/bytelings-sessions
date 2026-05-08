"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_add_item_basic():
    assert ex.add_item(1) == [1]


def test_add_item_no_aliasing():
    a = ex.add_item("first")
    b = ex.add_item("second")
    assert a == ["first"]
    assert b == ["second"]


def test_add_item_with_bucket():
    out = ex.add_item("x", [9])
    assert out == [9, "x"]


def test_merge_dicts_two():
    assert ex.merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_merge_dicts_collision():
    assert ex.merge_dicts({"a": 1}, {"a": 2}) == {"a": 2}


def test_merge_dicts_empty():
    assert ex.merge_dicts() == {}


def test_merge_dicts_does_not_mutate():
    a = {"a": 1}
    b = {"b": 2}
    ex.merge_dicts(a, b)
    assert a == {"a": 1}
    assert b == {"b": 2}


def test_call_with_extras_passes_kwargs():
    out = ex.call_with_extras(lambda x, y, z=0: (x, y, z), 1, 2, z=99)
    assert out == (1, 2, 99)


def test_call_with_extras_no_args():
    assert ex.call_with_extras(lambda: 42) == 42
