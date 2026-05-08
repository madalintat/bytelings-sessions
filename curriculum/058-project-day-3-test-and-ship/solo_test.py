"""HIDDEN tests for rung 4 — Day 3 final checkpoint."""
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
    p = request.url.path
    if p == "/ok":
        return httpx.Response(200, text="ok")
    if p == "/big":
        return httpx.Response(200, text="x" * 50)
    if p == "/notfound":
        return httpx.Response(404)
    if p == "/boom":
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
    assert s.status == 200 and s.body_length == 2


def test_fetch_records_connect_error():
    async def runner():
        async with _client() as c:
            return await ex.fetch(c, "http://t/boom")
    s = asyncio.run(runner())
    assert s.error == "ConnectError"


def test_snapshot_all_in_order():
    async def runner():
        async with _client() as c:
            return await ex.snapshot_all(c, [
                "http://t/ok", "http://t/big", "http://t/notfound"
            ])
    out = asyncio.run(runner())
    assert [s.url for s in out] == [
        "http://t/ok", "http://t/big", "http://t/notfound"
    ]


def test_snapshot_all_respects_concurrency_cap():
    """Wrap fetch so we can count concurrent calls."""
    state = {"current": 0, "peak": 0}

    real_fetch = ex.fetch

    async def counting_fetch(client, url):
        state["current"] += 1
        state["peak"] = max(state["peak"], state["current"])
        await asyncio.sleep(0.02)
        state["current"] -= 1
        return await real_fetch(client, url)

    ex.fetch = counting_fetch
    try:
        async def runner():
            async with _client() as c:
                return await ex.snapshot_all(
                    c, [f"http://t/ok" for _ in range(20)], max_in_flight=4
                )
        asyncio.run(runner())
        assert state["peak"] <= 4
    finally:
        ex.fetch = real_fetch


def test_save_snapshots(tmp_path):
    snaps = [
        ex.Snapshot(url="http://a", status=200, body_length=5),
        ex.Snapshot(url="http://b", status=0, error="ConnectError"),
    ]
    out = tmp_path / "snaps.json"
    ex.save_snapshots(out, snaps)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert data[0]["url"] == "http://a"


def test_save_atomic_no_tmp_left(tmp_path):
    out = tmp_path / "out.json"
    ex.save_snapshots(out, [ex.Snapshot(url="http://a")])
    assert list(tmp_path.glob("*.tmp")) == []
