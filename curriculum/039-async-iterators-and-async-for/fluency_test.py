"""Tests for rung 2."""
import asyncio
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_collect_basic():
    assert asyncio.run(ex.collect(3)) == [0, 1, 2]


def test_collect_zero():
    assert asyncio.run(ex.collect(0)) == []


def test_aticks_is_async_gen():
    import inspect
    assert inspect.isasyncgenfunction(ex.aticks)
