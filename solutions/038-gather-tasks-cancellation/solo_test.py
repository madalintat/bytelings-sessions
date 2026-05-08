"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import asyncio
import importlib.util
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


async def _ok(value):
    await asyncio.sleep(0.01)
    return value


async def _bad(exc_type):
    await asyncio.sleep(0.01)
    raise exc_type("boom")


def test_all_ok():
    result = asyncio.run(ex.fetch_all_safe([_ok(1), _ok(2), _ok(3)]))
    assert result == [1, 2, 3]


def test_some_raise():
    result = asyncio.run(ex.fetch_all_safe([_ok(1), _bad(ValueError), _ok(3)]))
    assert result == [1, "ERROR: ValueError", 3]


def test_all_raise():
    result = asyncio.run(ex.fetch_all_safe([_bad(KeyError), _bad(RuntimeError)]))
    assert result == ["ERROR: KeyError", "ERROR: RuntimeError"]


def test_empty():
    assert asyncio.run(ex.fetch_all_safe([])) == []


def test_runs_concurrently():
    coros = [_ok(i) for i in range(20)]
    t0 = time.perf_counter()
    asyncio.run(ex.fetch_all_safe(coros))
    elapsed = time.perf_counter() - t0
    assert elapsed < 0.20, "expected concurrent execution"
