"""Tests for rung 3."""
import hashlib
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_correctness_small():
    out = ex.parallel_hash(["a", "b", "c"])
    assert out == [hashlib.sha256(s.encode()).hexdigest() for s in ["a", "b", "c"]]


def test_in_order():
    items = [str(i) for i in range(20)]
    out = ex.parallel_hash(items, chunksize=4)
    expected = [hashlib.sha256(s.encode()).hexdigest() for s in items]
    assert out == expected


def test_uses_chunksize():
    src = inspect.getsource(ex.parallel_hash)
    assert "chunksize" in src, "pass chunksize through to pool.map"


def test_uses_process_pool():
    src = inspect.getsource(ex.parallel_hash)
    assert "ProcessPoolExecutor" in src
