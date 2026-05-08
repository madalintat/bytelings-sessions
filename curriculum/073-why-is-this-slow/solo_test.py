"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.find_pairs([1, 2, 3, 4, 5], 6) == [(1, 5), (2, 4)]


def test_no_pairs():
    assert ex.find_pairs([1, 2, 3], 100) == []


def test_duplicates_dedup():
    """Pair appears once, even if inputs duplicate."""
    assert ex.find_pairs([1, 5, 1, 5, 1], 6) == [(1, 5)]


def test_zero_target():
    assert ex.find_pairs([-2, 0, 2, 1, -1], 0) == [(-2, 2), (-1, 1)]


def test_perf_bound():
    """50K items must complete in well under a second with a set-based approach."""
    xs = list(range(50_000))
    start = time.perf_counter()
    out = ex.find_pairs(xs, 99_999)
    elapsed = time.perf_counter() - start
    # 99_999 = 0+99_999 = 1+99_998 ... but only pairs where both are < 50K count.
    # So no pairs at all, but the loop still runs full length.
    assert isinstance(out, list)
    assert elapsed < 1.0, (
        f"too slow ({elapsed:.2f}s) — use a set, not a nested loop"
    )
