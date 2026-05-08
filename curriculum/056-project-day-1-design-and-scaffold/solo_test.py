"""HIDDEN tests for rung 4 — Day 1 checkpoint."""
import asyncio
import importlib.util
import inspect
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _make_fake_fetch(delay=0.0, status=200):
    async def fake(url):
        await asyncio.sleep(delay)
        return ex.Snapshot(url=url, status=status, body_length=len(url))
    return fake


def test_returns_list():
    result = asyncio.run(ex.snapshot_all(["a", "b"], _make_fake_fetch()))
    assert isinstance(result, list)


def test_preserves_order():
    result = asyncio.run(ex.snapshot_all(["c", "a", "b"], _make_fake_fetch()))
    assert [s.url for s in result] == ["c", "a", "b"]


def test_runs_concurrently():
    """Five 50ms fetches should overlap, taking < 200ms total."""
    fake = _make_fake_fetch(delay=0.05)
    t0 = time.perf_counter()
    asyncio.run(ex.snapshot_all(["1", "2", "3", "4", "5"], fake))
    elapsed = time.perf_counter() - t0
    assert elapsed < 0.20


def test_empty_urls():
    assert asyncio.run(ex.snapshot_all([], _make_fake_fetch())) == []


def test_passes_through_errored_snapshots():
    async def errfetch(url):
        return ex.Snapshot(url=url, status=0, body_length=0, error="nope")
    result = asyncio.run(ex.snapshot_all(["x"], errfetch))
    assert len(result) == 1
    assert result[0].error == "nope"


def test_snapshot_all_is_async():
    assert inspect.iscoroutinefunction(ex.snapshot_all)
