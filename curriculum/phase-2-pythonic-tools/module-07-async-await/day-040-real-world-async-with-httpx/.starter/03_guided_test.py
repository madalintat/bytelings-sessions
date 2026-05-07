"""Tests for rung 3."""
import asyncio
import importlib.util
import time
from pathlib import Path

import httpx

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _slow_handler(request):
    # No real sleep here — but the test for concurrency uses an async handler.
    path = request.url.path
    if path == "/a":
        return httpx.Response(200)
    if path == "/b":
        return httpx.Response(201)
    if path == "/c":
        return httpx.Response(404)
    return httpx.Response(500)


def _client():
    return httpx.AsyncClient(
        transport=httpx.MockTransport(_slow_handler),
        base_url="http://test",
    )


def test_basic():
    async def runner():
        async with _client() as c:
            return await ex.fetch_many(c, [
                "http://test/a",
                "http://test/b",
                "http://test/c",
            ])
    result = asyncio.run(runner())
    assert result == [
        ("http://test/a", 200),
        ("http://test/b", 201),
        ("http://test/c", 404),
    ]


def test_empty():
    async def runner():
        async with _client() as c:
            return await ex.fetch_many(c, [])
    assert asyncio.run(runner()) == []


def test_preserves_input_order():
    async def runner():
        async with _client() as c:
            return await ex.fetch_many(c, [
                "http://test/c",
                "http://test/a",
                "http://test/b",
            ])
    out = asyncio.run(runner())
    assert [u for u, _ in out] == ["http://test/c", "http://test/a", "http://test/b"]
