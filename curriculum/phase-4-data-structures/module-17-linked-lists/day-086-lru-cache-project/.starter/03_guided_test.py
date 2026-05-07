"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_capacity_must_be_positive():
    with pytest.raises(ValueError):
        ex.LRUCache(0)


def test_get_miss_returns_none():
    c = ex.LRUCache(2)
    assert c.get("nope") is None


def test_put_then_get():
    c = ex.LRUCache(2)
    c.put("a", 1)
    assert c.get("a") == 1


def test_update_existing_key():
    c = ex.LRUCache(2)
    c.put("a", 1)
    c.put("a", 2)
    assert c.get("a") == 2
    assert len(c) == 1


def test_eviction_lru_after_get():
    c = ex.LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")        # touch "a", "b" is now LRU
    c.put("c", 3)     # should evict "b"
    assert c.get("b") is None
    assert c.get("a") == 1
    assert c.get("c") == 3


def test_eviction_pure_insert_order():
    c = ex.LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)     # evicts "a"
    assert c.get("a") is None
    assert c.get("b") == 2
    assert c.get("c") == 3


def test_len_capped_at_capacity():
    c = ex.LRUCache(3)
    for i, k in enumerate("abcdef"):
        c.put(k, i)
    assert len(c) == 3


def test_capacity_one():
    c = ex.LRUCache(1)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") is None
    assert c.get("b") == 2
