"""Tests for rung 3."""
import asyncio
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


async def _src(items):
    for x in items:
        await asyncio.sleep(0.0)
        yield x


async def _collect(agen):
    out = []
    async for v in agen:
        out.append(v)
    return out


def test_basic():
    assert asyncio.run(_collect(ex.aeven(_src([1, 2, 3, 4, 5])))) == [2, 4]


def test_no_evens():
    assert asyncio.run(_collect(ex.aeven(_src([1, 3, 5])))) == []


def test_all_evens():
    assert asyncio.run(_collect(ex.aeven(_src([2, 4, 6])))) == [2, 4, 6]


def test_empty_source():
    assert asyncio.run(_collect(ex.aeven(_src([])))) == []
