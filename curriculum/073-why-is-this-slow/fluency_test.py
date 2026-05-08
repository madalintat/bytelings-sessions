"""Tests for rung 2 — correctness + a (lenient) perf bound."""
import importlib.util
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.unique_preserve_order([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]


def test_empty():
    assert ex.unique_preserve_order([]) == []


def test_strings():
    assert ex.unique_preserve_order(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_perf_bound():
    """50K items with many duplicates must complete in << 1 second."""
    data = list(range(5_000)) * 10  # 50K items
    start = time.perf_counter()
    out = ex.unique_preserve_order(data)
    elapsed = time.perf_counter() - start
    assert out == list(range(5_000))
    assert elapsed < 1.0, (
        f"too slow ({elapsed:.2f}s) — switch `seen` from list to set"
    )
