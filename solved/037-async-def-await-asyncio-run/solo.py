"""Rung 4: Solo — solved version.

`fake_fetch` simulates one network hop with `asyncio.sleep(0.01)` and
returns a dict. `fetch_all` awaits each call in a plain `for` loop —
the sequential pattern. This guarantees input order at the cost of
latency; Day 38 introduces `gather` for concurrency.
"""
import asyncio


async def fake_fetch(item_id: int) -> dict:
    await asyncio.sleep(0.01)
    return {"id": item_id, "value": item_id * 10}


async def fetch_all(ids: list[int]) -> list[dict]:
    results = []
    for item_id in ids:
        results.append(await fake_fetch(item_id))
    return results
