"""Tests for rung 3."""
import importlib.util
import inspect
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.format_pairs([]) == ""


def test_single_pair():
    assert ex.format_pairs([("a", "1")]) == "a=1"


def test_multiple_pairs():
    out = ex.format_pairs([("a", "1"), ("b", "2"), ("c", "3")])
    assert out == "a=1; b=2; c=3"


def test_uses_join_not_plus():
    src = inspect.getsource(ex.format_pairs)
    assert ".join(" in src, "use ' '.join(parts) — not += in a loop"


def test_perf_bound():
    pairs = [(f"k{i}", str(i)) for i in range(100_000)]
    start = time.perf_counter()
    out = ex.format_pairs(pairs)
    elapsed = time.perf_counter() - start
    assert len(out) > 0
    assert elapsed < 1.5, (
        f"too slow ({elapsed:.2f}s) — string += in a loop is O(n^2); use join"
    )
