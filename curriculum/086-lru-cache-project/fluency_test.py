"""Tests for rung 2."""
import importlib.util
from collections import OrderedDict
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_touch_moves_to_front():
    c: OrderedDict = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    ex.touch(c, "b")
    # "b" should now be at the front
    assert list(c.keys()) == ["b", "a", "c"]


def test_touch_missing_is_noop():
    c: OrderedDict = OrderedDict([("a", 1), ("b", 2)])
    ex.touch(c, "z")
    assert list(c.keys()) == ["a", "b"]


def test_evict_one_drops_lru():
    c: OrderedDict = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    # "c" is the back (LRU), since "a" was inserted first then we'd
    # have touched things — but here, no touches; back is "c"
    ex.evict_one(c)
    assert list(c.keys()) == ["a", "b"]


def test_evict_empty_is_noop():
    c: OrderedDict = OrderedDict()
    ex.evict_one(c)
    assert len(c) == 0
