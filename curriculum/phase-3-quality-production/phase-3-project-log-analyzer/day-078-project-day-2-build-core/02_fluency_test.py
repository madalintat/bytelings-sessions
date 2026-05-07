"""Tests for rung 2."""
import importlib.util
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_merge_counts():
    a = ex.Aggregate(parsed=3, skipped=1)
    b = ex.Aggregate(parsed=4, skipped=2)
    out = a.merge(b)
    assert out.parsed == 7
    assert out.skipped == 3


def test_merge_counters():
    a = ex.Aggregate(levels=Counter({"INFO": 2}), top_paths=Counter({"/x": 1}))
    b = ex.Aggregate(levels=Counter({"INFO": 3, "ERROR": 1}), top_paths=Counter({"/x": 4, "/y": 2}))
    out = a.merge(b)
    assert out.levels == Counter({"INFO": 5, "ERROR": 1})
    assert out.top_paths == Counter({"/x": 5, "/y": 2})


def test_merge_does_not_mutate_originals():
    a = ex.Aggregate(parsed=1, levels=Counter({"INFO": 1}))
    b = ex.Aggregate(parsed=2, levels=Counter({"ERROR": 1}))
    a.merge(b)
    assert a.parsed == 1
    assert a.levels == Counter({"INFO": 1})
    assert b.parsed == 2
