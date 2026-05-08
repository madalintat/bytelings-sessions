"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_empty():
    assert ex.invert({}) == {}


def test_collision_last_wins():
    assert ex.invert({"a": 1, "b": 1}) == {1: "b"}


def test_string_values():
    assert ex.invert({"x": "X", "y": "Y"}) == {"X": "x", "Y": "y"}


def test_does_not_mutate_input():
    src = {"a": 1, "b": 2}
    ex.invert(src)
    assert src == {"a": 1, "b": 2}


def test_returns_new_dict():
    src = {"a": 1}
    out = ex.invert(src)
    assert out is not src
