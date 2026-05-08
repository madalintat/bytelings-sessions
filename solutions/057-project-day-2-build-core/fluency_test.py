"""Tests for rung 2."""
import asyncio
import importlib.util
from pathlib import Path

import httpx

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _handler(request):
    if request.url.path == "/ok":
        return httpx.Response(200, text="hello world")
    if request.url.path == "/missing":
        return httpx.Response(404, text="not found")
    if request.url.path == "/boom":
        raise httpx.ConnectError("offline", request=request)
    return httpx.Response(500)


def _client():
    return httpx.AsyncClient(
        transport=httpx.MockTransport(_handler),
        base_url="http://t",
    )


def test_success():
    async def runner():
        async with _client() as c:
            return await ex.fetch(c, "http://t/ok")
    s = asyncio.run(runner())
    assert s.url == "http://t/ok"
    assert s.status == 200
    assert s.body_length == len("hello world")
    assert s.error is None


def test_404_is_not_an_error():
    """A non-2xx response is still a successful HTTP exchange."""
    async def runner():
        async with _client() as c:
            return await ex.fetch(c, "http://t/missing")
    s = asyncio.run(runner())
    assert s.status == 404
    assert s.error is None


def test_network_error_records_error_field():
    async def runner():
        async with _client() as c:
            return await ex.fetch(c, "http://t/boom")
    s = asyncio.run(runner())
    assert s.status == 0
    assert s.body_length == 0
    assert s.error == "ConnectError"
