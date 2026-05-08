"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_put_get():
    m = ex.HashMapOA()
    m.put("alice", 31)
    assert m.get("alice") == 31


def test_get_missing_raises():
    m = ex.HashMapOA()
    with pytest.raises(KeyError):
        m.get("nope")


def test_put_overwrites():
    m = ex.HashMapOA()
    m.put("a", 1)
    m.put("a", 99)
    assert m.get("a") == 99
    assert len(m) == 1


def test_pop_then_lookup():
    m = ex.HashMapOA()
    m.put("a", 1)
    m.put("b", 2)
    assert m.pop("a") == 1
    with pytest.raises(KeyError):
        m.get("a")


def test_pop_missing_raises():
    m = ex.HashMapOA()
    with pytest.raises(KeyError):
        m.pop("nope")


def test_pop_then_other_keys_still_findable():
    """The tombstone test: deleting one key must NOT break lookup
    for keys whose probe path passes through that slot."""
    m = ex.HashMapOA()
    # Force a chain: insert many keys; pop one; the rest should still resolve.
    for i in range(50):
        m.put(f"key-{i}", i)
    m.pop("key-10")
    for i in range(50):
        if i == 10:
            continue
        assert m.get(f"key-{i}") == i


def test_re_insert_reuses_tombstone():
    m = ex.HashMapOA()
    m.put("a", 1)
    m.pop("a")
    m.put("a", 2)
    assert m.get("a") == 2
    assert len(m) == 1


def test_many_inserts_and_resize():
    m = ex.HashMapOA()
    for i in range(500):
        m.put(i, i * i)
    for i in range(500):
        assert m.get(i) == i * i
    assert len(m) == 500
    # Capacity grew well past the initial 8.
    assert m._capacity() > 8


def test_iter_yields_only_live_keys():
    m = ex.HashMapOA()
    for k in ["a", "b", "c", "d", "e"]:
        m.put(k, 1)
    m.pop("c")
    assert sorted(list(m)) == ["a", "b", "d", "e"]


def test_contains_after_pop():
    m = ex.HashMapOA()
    m.put("a", 1)
    m.pop("a")
    assert ("a" in m) is False
