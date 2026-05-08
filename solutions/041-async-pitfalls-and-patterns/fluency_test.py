"""Tests for rung 2."""
import asyncio
import importlib.util
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_correct_values():
    assert asyncio.run(ex.bulk_double([1, 2, 3])) == [2, 4, 6]


def test_runs_concurrently():
    """5 x 50ms must overlap — well under 250ms when both bugs are fixed."""
    t0 = time.perf_counter()
    asyncio.run(ex.bulk_double([1, 2, 3, 4, 5]))
    elapsed = time.perf_counter() - t0
    assert elapsed < 0.20, (
        f"took {elapsed:.2f}s — still blocking or still sequential"
    )


def test_no_blocking_sleep():
    """time.sleep in async code freezes the event loop. Use asyncio.sleep."""
    src = (_HERE / "02_fluency.py").read_text()
    assert "time.sleep(" not in src, (
        "time.sleep is blocking; use `await asyncio.sleep(...)` instead"
    )
