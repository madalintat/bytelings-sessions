"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


E = ex.EMPTY
T = ex.TOMB


def kv(x):
    return (x, x)


def test_all_empty():
    assert ex.cluster_lengths([E] * 8) == []


def test_all_full():
    # one big cluster; wraps trivially since there's no empty slot.
    out = ex.cluster_lengths([kv(i) for i in range(8)])
    assert sorted(out) == [8]


def test_two_clusters_no_wrap():
    slots = [kv("a"), E, kv("b"), kv("c"), E, E, E, E]
    out = ex.cluster_lengths(slots)
    assert sorted(out) == [1, 2]


def test_tombs_count_as_occupied():
    slots = [E, kv("a"), T, kv("b"), E, E, kv("c"), kv("d")]
    out = ex.cluster_lengths(slots)
    assert sorted(out) == [2, 3]


def test_wrap_around_is_single_cluster():
    # 6, 7, 0, 1 are occupied; 2..5 empty -> one cluster of length 4
    slots = [kv("a"), kv("b"), E, E, E, E, kv("c"), kv("d")]
    out = ex.cluster_lengths(slots)
    assert sorted(out) == [4]


def test_single_occupied_slot():
    slots = [E] * 8
    slots[3] = kv("x")
    assert ex.cluster_lengths(slots) == [1]


def test_only_tombstones():
    slots = [T] * 4
    out = ex.cluster_lengths(slots)
    assert sorted(out) == [4]


def test_no_wrap_when_one_empty_at_zero():
    slots = [E, kv("a"), kv("b"), kv("c"), E, kv("d"), kv("e"), E]
    out = ex.cluster_lengths(slots)
    assert sorted(out) == [2, 3]
