"""Rung 2: Fluency — solved version.

`asyncio.gather(*coros)` launches all coroutines concurrently and
returns their results in input order. Replacing the sequential
`await` loop with `gather` means all `_slow_double` calls overlap
on the event loop — total wall time is ~50 ms instead of 50*n ms.
"""
import asyncio


async def _slow_double(n: int) -> int:
    await asyncio.sleep(0.05)
    return n * 2


async def fetch_all(ns: list[int]) -> list[int]:
    """Return [n*2 for n in ns], with all calls concurrent."""
    return list(await asyncio.gather(*(_slow_double(n) for n in ns)))
