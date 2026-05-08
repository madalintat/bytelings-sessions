"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_disjoint():
    p = [{"id": 1, "name": "A"}]
    s = [{"id": 2, "name": "B"}]
    assert ex.merge_rosters(p, s) == [
        {"id": 1, "name": "A"},
        {"id": 2, "name": "B"},
    ]


def test_overlap_secondary_wins():
    p = [{"id": 1, "name": "A", "tag": "p"}, {"id": 2, "name": "B"}]
    s = [{"id": 1, "name": "A2"}, {"id": 3, "name": "C"}]
    assert ex.merge_rosters(p, s) == [
        {"id": 1, "name": "A2", "tag": "p"},
        {"id": 2, "name": "B"},
        {"id": 3, "name": "C"},
    ]


def test_empty_primary():
    s = [{"id": 1, "name": "X"}]
    assert ex.merge_rosters([], s) == [{"id": 1, "name": "X"}]


def test_empty_secondary():
    p = [{"id": 1, "name": "X"}]
    assert ex.merge_rosters(p, []) == [{"id": 1, "name": "X"}]


def test_both_empty():
    assert ex.merge_rosters([], []) == []


def test_does_not_mutate():
    p = [{"id": 1, "name": "A"}]
    s = [{"id": 1, "name": "B"}]
    p_copy = [dict(d) for d in p]
    s_copy = [dict(d) for d in s]
    ex.merge_rosters(p, s)
    assert p == p_copy
    assert s == s_copy


def test_secondary_only_keys_added():
    p = [{"id": 1, "name": "A"}]
    s = [{"id": 1, "extra": 42}]
    assert ex.merge_rosters(p, s) == [{"id": 1, "name": "A", "extra": 42}]
