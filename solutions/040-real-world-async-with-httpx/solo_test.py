"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import asyncio
import importlib.util
from pathlib import Path

import httpx

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _handler(request):
    path = request.url.path
    if path == "/ok":
        return httpx.Response(200)
    if path == "/created":
        return httpx.Response(201)
    if path == "/notfound":
        return httpx.Response(404)
    if path == "/server":
        return httpx.Response(500)
    if path == "/boom":
        raise httpx.ConnectError("boom", request=request)
    return httpx.Response(599)


def _client():
    return httpx.AsyncClient(
        transport=httpx.MockTransport(_handler),
        base_url="http://t",
    )


def test_all_ok():
    async def runner():
        async with _client() as c:
            return await ex.health_report(c, ["http://t/ok", "http://t/created"])
    assert asyncio.run(runner()) == {
        "http://t/ok": "ok",
        "http://t/created": "ok",
    }


def test_bad_status():
    async def runner():
        async with _client() as c:
            return await ex.health_report(c, ["http://t/notfound", "http://t/server"])
    assert asyncio.run(runner()) == {
        "http://t/notfound": "bad",
        "http://t/server": "bad",
    }


def test_exception_becomes_error():
    async def runner():
        async with _client() as c:
            return await ex.health_report(c, ["http://t/boom"])
    assert asyncio.run(runner()) == {"http://t/boom": "error"}


def test_mixed():
    async def runner():
        async with _client() as c:
            return await ex.health_report(c, [
                "http://t/ok",
                "http://t/notfound",
                "http://t/boom",
            ])
    assert asyncio.run(runner()) == {
        "http://t/ok": "ok",
        "http://t/notfound": "bad",
        "http://t/boom": "error",
    }


def test_empty():
    async def runner():
        async with _client() as c:
            return await ex.health_report(c, [])
    assert asyncio.run(runner()) == {}
