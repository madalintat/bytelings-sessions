"""Rung 2: Fluency — solved version.

Two bugs fixed:
1. `fake_fetch` used `time.sleep` which blocks the entire event loop
   thread. `await asyncio.sleep(0.05)` yields control back to the loop
   so other coroutines can run during the wait.
2. `bulk_double` awaited each coroutine sequentially inside a `for`
   loop. `asyncio.gather(*coros)` launches them all at once and returns
   when the last one finishes, cutting wall time from 5×50ms to ~50ms.
"""
import asyncio


async def fake_fetch(n: int) -> int:
    await asyncio.sleep(0.05)
    return n * 2


async def bulk_double(ns: list[int]) -> list[int]:
    """Return [n*2 for n in ns], concurrently."""
    coros = [fake_fetch(n) for n in ns]
    return list(await asyncio.gather(*coros))
