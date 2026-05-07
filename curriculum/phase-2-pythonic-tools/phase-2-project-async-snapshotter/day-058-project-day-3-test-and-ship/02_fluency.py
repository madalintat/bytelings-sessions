"""Rung 2: Fluency drill — bound the concurrency.

Topic: project polish, Day 3

`snapshot_all_bounded(fetch_fn, urls, limit)` should:
1. Build a semaphore with `limit` slots.
2. For each url, call fetch_fn(url) inside `async with sem:`.
3. Run all of them via asyncio.gather and return results in input order.

The current implementation has no semaphore — fix it.
"""
import asyncio


async def snapshot_all_bounded(fetch_fn, urls: list[str], limit: int) -> list:
    """Concurrent calls to fetch_fn(url), capped at `limit` in flight."""
    # TODO: introduce an asyncio.Semaphore(limit) and use `async with sem:`
    # inside a wrapper that defers to fetch_fn(url).
    return await asyncio.gather(*(fetch_fn(u) for u in urls))
