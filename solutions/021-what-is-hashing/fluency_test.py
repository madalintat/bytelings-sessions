"""Tests for rung 2 — toy hashmap."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_buckets_are_independent():
    """[[]]*n creates aliased slots — appending to one would touch all."""
    t = ex.Tiny(n_buckets=4)
    t.buckets[0].append("MARK")
    assert t.buckets[1] == [], "buckets must be independent lists"


def test_set_and_get():
    t = ex.Tiny()
    t.set("a", 1)
    t.set("b", 2)
    assert t.get("a") == 1
    assert t.get("b") == 2


def test_get_missing_returns_default():
    t = ex.Tiny()
    assert t.get("nope") is None
    assert t.get("nope", default=42) == 42


def test_overwrite():
    t = ex.Tiny()
    t.set("a", 1)
    t.set("a", 99)
    assert t.get("a") == 99


def test_contains():
    t = ex.Tiny()
    t.set("a", 1)
    assert "a" in t
    assert "b" not in t


def test_handles_collisions():
    """Force several keys into the same bucket by making a tiny table."""
    t = ex.Tiny(n_buckets=2)
    for i in range(20):
        t.set(f"k{i}", i)
    for i in range(20):
        assert t.get(f"k{i}") == i


def test_get_missing_in_populated_bucket():
    """Even with stuff in the bucket, a missing key returns the default."""
    t = ex.Tiny(n_buckets=1)  # everything collides
    t.set("a", 1)
    t.set("b", 2)
    assert t.get("c") is None
