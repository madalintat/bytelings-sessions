"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_probe_next_basic():
    assert ex.probe_next(0, 8) == 1


def test_probe_next_middle():
    assert ex.probe_next(3, 8) == 4


def test_probe_next_wraps():
    assert ex.probe_next(7, 8) == 0
    assert ex.probe_next(15, 16) == 0


def test_find_slot_returns_empty_when_missing():
    slots = [ex.EMPTY] * 8
    idx = ex.find_slot(slots, "alice")
    assert slots[idx] is ex.EMPTY


def test_find_slot_returns_match():
    slots = [ex.EMPTY] * 8
    home = hash("alice") % 8
    slots[home] = ("alice", 31)
    idx = ex.find_slot(slots, "alice")
    assert idx == home


def test_find_slot_walks_past_other_keys():
    # Force a collision: place a different key at "alice"'s home slot.
    slots = [ex.EMPTY] * 8
    home = hash("alice") % 8
    slots[home] = ("dummy", 0)
    next_slot = (home + 1) % 8
    slots[next_slot] = ("alice", 31)
    idx = ex.find_slot(slots, "alice")
    assert idx == next_slot


def test_find_slot_walks_past_tombstone():
    slots = [ex.EMPTY] * 8
    home = hash("alice") % 8
    slots[home] = ex.TOMB
    next_slot = (home + 1) % 8
    slots[next_slot] = ("alice", 31)
    idx = ex.find_slot(slots, "alice")
    assert idx == next_slot
