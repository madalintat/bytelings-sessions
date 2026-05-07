"""Tests for rung 2."""
import asyncio
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _make_tracker(delay=0.01):
    state = {"current": 0, "peak": 0}

    async def fetch_fn(url):
        state["current"] += 1
        state["peak"] = max(state["peak"], state["current"])
        await asyncio.sleep(delay)
        state["current"] -= 1
        return url

    return state, fetch_fn


def test_returns_results_in_order():
    state, fetch_fn = _make_tracker()
    urls = [f"u{i}" for i in range(10)]
    result = asyncio.run(ex.snapshot_all_bounded(fetch_fn, urls, 3))
    assert result == urls


def test_respects_limit():
    state, fetch_fn = _make_tracker()
    urls = [f"u{i}" for i in range(20)]
    asyncio.run(ex.snapshot_all_bounded(fetch_fn, urls, 4))
    assert state["peak"] <= 4


def test_empty():
    state, fetch_fn = _make_tracker()
    assert asyncio.run(ex.snapshot_all_bounded(fetch_fn, [], 5)) == []
