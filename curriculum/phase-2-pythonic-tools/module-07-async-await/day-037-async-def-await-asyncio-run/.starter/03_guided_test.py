"""Tests for rung 3."""
import asyncio
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_is_async():
    assert inspect.iscoroutinefunction(ex.greet_after)


def test_basic():
    assert asyncio.run(ex.greet_after("Mada", 0.0)) == "Hello, Mada!"


def test_empty_name():
    assert asyncio.run(ex.greet_after("", 0.0)) == "Hello, !"


def test_actually_sleeps():
    import time
    t0 = time.perf_counter()
    asyncio.run(ex.greet_after("x", 0.05))
    assert (time.perf_counter() - t0) >= 0.04
