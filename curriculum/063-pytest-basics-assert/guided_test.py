"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_unseen_key_is_zero():
    c = ex.Counter()
    assert c.value("api/users") == 0


def test_hit_returns_new_value():
    c = ex.Counter()
    assert c.hit("a") == 1
    assert c.hit("a") == 2
    assert c.hit("a") == 3


def test_independent_keys():
    c = ex.Counter()
    c.hit("a")
    c.hit("a")
    c.hit("b")
    assert c.value("a") == 2
    assert c.value("b") == 1


def test_reset_clears_one_key():
    c = ex.Counter()
    c.hit("a")
    c.hit("b")
    c.reset("a")
    assert c.value("a") == 0
    assert c.value("b") == 1


def test_reset_unseen_no_error():
    c = ex.Counter()
    c.reset("never seen")
    assert c.value("never seen") == 0


def test_hit_after_reset_starts_at_one():
    c = ex.Counter()
    c.hit("a")
    c.hit("a")
    c.reset("a")
    assert c.hit("a") == 1
