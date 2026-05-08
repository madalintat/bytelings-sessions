"""Tests for rung 2 — correctness + structural check.

We don't impose a perf bound here because it's environment-dependent;
the structural check verifies you switched the executor.
"""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_correctness():
    out = ex.hash_many(["a", "b", "c"])
    assert len(out) == 3
    assert all(len(h) == 64 for h in out)
    # deterministic
    assert ex.hash_many(["a"])[0] == out[0]


def test_uses_process_pool():
    src = inspect.getsource(ex.hash_many)
    assert "ProcessPoolExecutor" in src, (
        "switch to ProcessPoolExecutor — threads don't help CPU-bound work"
    )
    assert "ThreadPoolExecutor" not in src, (
        "remove the ThreadPoolExecutor — wrong pool for CPU work"
    )
