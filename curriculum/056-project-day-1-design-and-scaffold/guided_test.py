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


def test_fetch_is_async():
    assert inspect.iscoroutinefunction(ex.fetch)


def test_fetch_returns_snapshot():
    result = asyncio.run(ex.fetch(client=None, url="http://x"))
    assert isinstance(result, ex.Snapshot)


def test_fetch_records_url():
    result = asyncio.run(ex.fetch(client=None, url="http://example.com"))
    assert result.url == "http://example.com"


def test_fetch_stub_indicates_not_implemented():
    result = asyncio.run(ex.fetch(client=None, url="http://x"))
    assert result.status == 0
    assert result.body_length == 0
    assert result.error == "not implemented yet"
