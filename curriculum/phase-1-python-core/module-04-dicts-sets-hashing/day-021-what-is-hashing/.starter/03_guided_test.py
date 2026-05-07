"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_len_starts_at_zero():
    t = ex.Tiny()
    assert len(t) == 0


def test_len_grows():
    t = ex.Tiny()
    t.set("a", 1)
    t.set("b", 2)
    assert len(t) == 2


def test_len_overwrite_does_not_grow():
    t = ex.Tiny()
    t.set("a", 1)
    t.set("a", 2)
    assert len(t) == 1


def test_delete_present():
    t = ex.Tiny()
    t.set("a", 1)
    assert t.delete("a") is True
    assert t.get("a") is None


def test_delete_absent():
    t = ex.Tiny()
    assert t.delete("nope") is False


def test_delete_decrements_len():
    t = ex.Tiny()
    t.set("a", 1)
    t.set("b", 2)
    t.delete("a")
    assert len(t) == 1


def test_delete_in_collision_bucket():
    t = ex.Tiny(n_buckets=1)  # everything collides
    t.set("a", 1)
    t.set("b", 2)
    t.set("c", 3)
    assert t.delete("b") is True
    assert t.get("a") == 1
    assert t.get("b") is None
    assert t.get("c") == 3
    assert len(t) == 2
