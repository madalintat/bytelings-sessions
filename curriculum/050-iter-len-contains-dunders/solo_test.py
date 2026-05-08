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
    s = ex.OrderedSet([1, 2, 3])
    assert list(s) == [1, 2, 3]


def test_dedupes_on_init():
    s = ex.OrderedSet([1, 2, 1, 3, 2])
    assert list(s) == [1, 2, 3]


def test_add():
    s = ex.OrderedSet()
    s.add(1)
    s.add(2)
    s.add(1)
    assert list(s) == [1, 2]


def test_len():
    assert len(ex.OrderedSet([1, 2, 3, 1])) == 3
    assert len(ex.OrderedSet()) == 0


def test_contains():
    s = ex.OrderedSet([1, 2, 3])
    assert 2 in s
    assert 99 not in s


def test_repr():
    s = ex.OrderedSet([1, 2])
    assert repr(s) == "OrderedSet([1, 2])"


def test_contains_is_fast():
    """Building 100k items + checking membership should be ~milliseconds, not seconds."""
    s = ex.OrderedSet(range(100_000))
    t0 = time.perf_counter()
    for q in [0, 50_000, 99_999, 100_000]:
        _ = q in s
    elapsed = time.perf_counter() - t0
    assert elapsed < 0.05, (
        f"`in` took {elapsed:.3f}s — back it with a set/dict for O(1) lookup"
    )
