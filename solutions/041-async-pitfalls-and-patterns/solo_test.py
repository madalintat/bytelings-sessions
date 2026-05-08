"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import asyncio
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_succeeds_first_try():
    async def good():
        return "ok"
    assert asyncio.run(ex.retry(good, 3, 0.0)) == "ok"


def test_succeeds_after_retries():
    state = {"n": 0}

    async def flaky():
        state["n"] += 1
        if state["n"] < 3:
            raise RuntimeError("nope")
        return "ok"

    assert asyncio.run(ex.retry(flaky, 5, 0.0)) == "ok"
    assert state["n"] == 3


def test_all_attempts_fail():
    async def always_bad():
        raise ValueError("doomed")

    with pytest.raises(ValueError):
        asyncio.run(ex.retry(always_bad, 3, 0.0))


def test_factory_is_called_each_attempt():
    state = {"n": 0}

    async def flaky():
        state["n"] += 1
        raise RuntimeError("x")

    with pytest.raises(RuntimeError):
        asyncio.run(ex.retry(flaky, 4, 0.0))
    assert state["n"] == 4


def test_zero_attempts_raises_or_signals():
    """0 attempts means we never even try. Either raise or return is fine,
    as long as it doesn't loop forever and doesn't call the factory."""
    state = {"n": 0}

    async def good():
        state["n"] += 1
        return "ok"

    try:
        asyncio.run(ex.retry(good, 0, 0.0))
    except Exception:
        pass
    assert state["n"] == 0
