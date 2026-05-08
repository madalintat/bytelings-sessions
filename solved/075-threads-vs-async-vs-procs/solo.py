"""Rung 4: Solo implement — solved version.

async_gather_lengths uses asyncio.gather to run all fetcher coroutines
concurrently and returns the lengths in input order. run_sync wraps it
with asyncio.run() for sync callers.
"""
import asyncio
from typing import Awaitable, Callable


async def async_gather_lengths(
    urls: list[str],
    fetcher: Callable[[str], Awaitable[str]],
) -> list[int]:
    results = await asyncio.gather(*(fetcher(url) for url in urls))
    return [len(r) for r in results]


def run_sync(
    urls: list[str],
    fetcher: Callable[[str], Awaitable[str]],
) -> list[int]:
    return asyncio.run(async_gather_lengths(urls, fetcher))
