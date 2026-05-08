"""Rung 2: Fluency — solved version.

`snapshot_all_bounded` wraps each `fetch_fn(url)` call in a helper
that acquires a `Semaphore` before awaiting. `asyncio.gather` then
starts all wrappers; the semaphore ensures at most `limit` are active
at any time.
"""
import asyncio


async def snapshot_all_bounded(fetch_fn, urls: list[str], limit: int) -> list:
    """Concurrent calls to fetch_fn(url), capped at `limit` in flight."""
    sem = asyncio.Semaphore(limit)

    async def _guarded(url):
        async with sem:
            return await fetch_fn(url)

    return list(await asyncio.gather(*(_guarded(u) for u in urls)))
