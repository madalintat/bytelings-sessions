"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert list(ex.iter_keys({})) == []


def test_flat():
    got = sorted(ex.iter_keys({"a": 1, "b": 2}))
    assert got == ["a", "b"]


def test_one_level():
    got = sorted(ex.iter_keys({"a": 1, "b": {"c": 2}}))
    assert got == ["a", "b.c"]


def test_deep():
    d = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
    got = sorted(ex.iter_keys(d))
    assert got == ["a", "b.c", "b.d.e"]


def test_very_deep_no_recursion_error():
    """Build a 2000-deep dict — would blow recursion limit if you recursed."""
    d = current = {}
    for i in range(2000):
        nxt = {}
        current["k"] = nxt
        current = nxt
    current["leaf"] = 42
    keys = list(ex.iter_keys(d))
    assert len(keys) == 1
    assert keys[0].endswith(".leaf")
