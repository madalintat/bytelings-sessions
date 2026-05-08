"""Tests for rung 2."""
import asyncio
import importlib.util
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_correct_results():
    assert asyncio.run(ex.fetch_all([1, 2, 3, 4])) == [2, 4, 6, 8]


def test_empty():
    assert asyncio.run(ex.fetch_all([])) == []


def test_runs_concurrently():
    """Five 50ms fetches should take ~50ms concurrently, not ~250ms sequentially."""
    t0 = time.perf_counter()
    asyncio.run(ex.fetch_all([1, 2, 3, 4, 5]))
    elapsed = time.perf_counter() - t0
    assert elapsed < 0.20, (
        f"fetch_all took {elapsed:.2f}s — looks sequential. Use asyncio.gather."
    )
