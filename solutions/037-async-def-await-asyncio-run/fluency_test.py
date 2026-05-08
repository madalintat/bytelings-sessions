"""Tests for rung 2."""
import asyncio
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_double_is_a_coroutine_function():
    assert inspect.iscoroutinefunction(ex.double), (
        "double must be `async def`"
    )


def test_double_returns_value():
    async def runner():
        return await ex.double(7)
    assert asyncio.run(runner()) == 14


def test_add_after_delay_returns_int():
    async def runner():
        return await ex.add_after_delay(2, 3, 0.0)
    result = asyncio.run(runner())
    assert result == 5
    assert isinstance(result, int)


def test_add_after_delay_actually_waits():
    """The await on asyncio.sleep should make the call take at least `delay` seconds."""
    import time

    async def runner():
        return await ex.add_after_delay(1, 1, 0.05)

    t0 = time.perf_counter()
    asyncio.run(runner())
    elapsed = time.perf_counter() - t0
    assert elapsed >= 0.04, (
        "add_after_delay returned too fast — did you await asyncio.sleep?"
    )
