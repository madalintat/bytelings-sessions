"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    m = ex.HashMap()
    assert len(m) == 0
    assert "anything" not in m


def test_put_and_get():
    m = ex.HashMap()
    m.put("alice", 31)
    m.put("bob", 22)
    assert m.get("alice") == 31
    assert m.get("bob") == 22
    assert len(m) == 2


def test_get_missing_raises():
    m = ex.HashMap()
    with pytest.raises(KeyError):
        m.get("nope")


def test_put_overwrites():
    m = ex.HashMap()
    m.put("alice", 1)
    m.put("alice", 99)
    assert m.get("alice") == 99
    assert len(m) == 1


def test_contains():
    m = ex.HashMap()
    m.put("a", 1)
    assert ("a" in m) is True
    assert ("b" in m) is False


def test_pop_basic():
    m = ex.HashMap()
    m.put("a", 1); m.put("b", 2)
    assert m.pop("a") == 1
    assert "a" not in m
    assert len(m) == 1


def test_pop_missing_raises():
    m = ex.HashMap()
    with pytest.raises(KeyError):
        m.pop("nope")


def test_iter_yields_all_keys():
    m = ex.HashMap()
    keys = ["alice", "bob", "carol", "dave"]
    for k in keys:
        m.put(k, k.upper())
    assert sorted(list(m)) == sorted(keys)


def test_resize_correctness():
    """Insert way more than INITIAL_CAPACITY items; everything should still be findable."""
    m = ex.HashMap()
    for i in range(200):
        m.put(f"key-{i}", i)
    for i in range(200):
        assert m.get(f"key-{i}") == i
    assert len(m) == 200


def test_resize_actually_grows():
    m = ex.HashMap()
    for i in range(50):
        m.put(i, i)
    # After 50 inserts, capacity should be > INITIAL_CAPACITY (8).
    assert len(m._slots) > 8


def test_int_keys_work():
    m = ex.HashMap()
    for i in range(20):
        m.put(i, i * i)
    for i in range(20):
        assert m.get(i) == i * i


def test_tuple_keys_work():
    m = ex.HashMap()
    m.put((1, 2), "one-two")
    m.put((1, 3), "one-three")
    assert m.get((1, 2)) == "one-two"
    assert m.get((1, 3)) == "one-three"
