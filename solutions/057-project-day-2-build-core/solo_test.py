"""HIDDEN tests for rung 4 — Day 2 checkpoint."""
import asyncio
import importlib.util
import json
import time
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
        return httpx.Response(200, text="aaa")
    if path == "/big":
        return httpx.Response(200, text="x" * 100)
    if path == "/notfound":
        return httpx.Response(404, text="nope")
    if path == "/boom":
        raise httpx.ConnectError("offline", request=request)
    return httpx.Response(500)


def _client():
    return httpx.AsyncClient(
        transport=httpx.MockTransport(_handler),
        base_url="http://t",
    )


def test_fetch_success():
    async def runner():
        async with _client() as c:
            return await ex.fetch(c, "http://t/ok")
    s = asyncio.run(runner())
    assert s.status == 200 and s.body_length == 3 and s.error is None


def test_fetch_network_error():
    async def runner():
        async with _client() as c:
            return await ex.fetch(c, "http://t/boom")
    s = asyncio.run(runner())
    assert s.error == "ConnectError"


def test_snapshot_all_basic():
    async def runner():
        async with _client() as c:
            return await ex.snapshot_all(c, ["http://t/ok", "http://t/big"])
    out = asyncio.run(runner())
    assert [s.url for s in out] == ["http://t/ok", "http://t/big"]
    assert out[0].body_length == 3
    assert out[1].body_length == 100


def test_snapshot_all_handles_mixed_errors():
    async def runner():
        async with _client() as c:
            return await ex.snapshot_all(
                c, ["http://t/ok", "http://t/boom", "http://t/notfound"]
            )
    out = asyncio.run(runner())
    assert out[0].status == 200 and out[0].error is None
    assert out[1].error == "ConnectError"
    assert out[2].status == 404 and out[2].error is None


def test_save_snapshots_writes_json(tmp_path):
    snaps = [ex.Snapshot(url="http://a", status=200, body_length=5)]
    out = tmp_path / "snaps.json"
    ex.save_snapshots(out, snaps)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data == [{"url": "http://a", "status": 200, "body_length": 5, "error": None}]


def test_save_is_atomic(tmp_path):
    out = tmp_path / "snaps.json"
    ex.save_snapshots(out, [ex.Snapshot(url="http://a")])
    leftovers = list(tmp_path.glob("*.tmp"))
    assert leftovers == []
