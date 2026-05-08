"""Tests for rung 3."""
import asyncio
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _make_tracker():
    state = {"current": 0, "peak": 0}

    async def task(value):
        state["current"] += 1
        state["peak"] = max(state["peak"], state["current"])
        await asyncio.sleep(0.02)
        state["current"] -= 1
        return value

    return state, task


def test_returns_correct_results_in_order():
    _state, task = _make_tracker()
    coros = [task(i) for i in range(8)]
    result = asyncio.run(ex.bounded_fetch(coros, 3))
    assert result == list(range(8))


def test_never_exceeds_limit():
    state, task = _make_tracker()
    coros = [task(i) for i in range(10)]
    asyncio.run(ex.bounded_fetch(coros, 3))
    assert state["peak"] <= 3


def test_empty():
    assert asyncio.run(ex.bounded_fetch([], 5)) == []


def test_limit_larger_than_jobs():
    _state, task = _make_tracker()
    result = asyncio.run(ex.bounded_fetch([task(i) for i in range(3)], 100))
    assert result == [0, 1, 2]
