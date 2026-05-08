"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import asyncio
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_both_are_coroutines():
    assert inspect.iscoroutinefunction(ex.fake_fetch)
    assert inspect.iscoroutinefunction(ex.fetch_all)


def test_fake_fetch_shape():
    result = asyncio.run(ex.fake_fetch(3))
    assert result == {"id": 3, "value": 30}


def test_fetch_all_basic():
    result = asyncio.run(ex.fetch_all([1, 2, 3]))
    assert result == [
        {"id": 1, "value": 10},
        {"id": 2, "value": 20},
        {"id": 3, "value": 30},
    ]


def test_fetch_all_empty():
    assert asyncio.run(ex.fetch_all([])) == []


def test_fetch_all_preserves_order():
    result = asyncio.run(ex.fetch_all([7, 2, 5]))
    assert [r["id"] for r in result] == [7, 2, 5]
