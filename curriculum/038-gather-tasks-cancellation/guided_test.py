"""Tests for rung 3."""
import asyncio
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


async def _quick():
    await asyncio.sleep(0.0)
    return "ok"


async def _slow():
    await asyncio.sleep(1.0)
    return "should-not-see-this"


def test_finishes_in_time():
    assert asyncio.run(ex.with_timeout(_quick(), 1.0)) == "ok"


def test_times_out():
    assert asyncio.run(ex.with_timeout(_slow(), 0.05)) == "TIMED_OUT"


def test_does_not_raise_on_timeout():
    # Should not raise — should return the sentinel.
    result = asyncio.run(ex.with_timeout(_slow(), 0.05))
    assert result == "TIMED_OUT"
