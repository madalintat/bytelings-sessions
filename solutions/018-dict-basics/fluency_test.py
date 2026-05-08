"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_lookup_present():
    assert ex.lookup({"a": 1}, "a") == 1


def test_lookup_missing_default():
    assert ex.lookup({"a": 1}, "b") is None
    assert ex.lookup({"a": 1}, "b", default="?") == "?"


def test_has_key():
    assert ex.has_key({"a": 1}, "a") is True
    assert ex.has_key({"a": 1}, "b") is False


def test_total_values():
    assert ex.total_values({"a": 1, "b": 2, "c": 3}) == 6
    assert ex.total_values({}) == 0


def test_to_pairs_order():
    d = {"x": 10, "y": 20, "z": 30}
    assert ex.to_pairs(d) == [("x", 10), ("y", 20), ("z", 30)]


def test_to_pairs_empty():
    assert ex.to_pairs({}) == []
