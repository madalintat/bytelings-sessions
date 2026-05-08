"""Rung 2: Fluency drill — find the two bugs.

Topic: async pitfalls (blocking sleep, sequential await loop)

`bulk_double` runs 5 fake fetches and returns their doubled values.
Both bugs from the concept page are present. Fix them both.
"""
import asyncio
import time


async def fake_fetch(n: int) -> int:
    # TODO: time.sleep blocks the event loop. Replace with await asyncio.sleep.
    time.sleep(0.05)
    return n * 2


async def bulk_double(ns: list[int]) -> list[int]:
    """Return [n*2 for n in ns], concurrently."""
    coros = [fake_fetch(n) for n in ns]
    # TODO: this for-loop awaits sequentially. Use asyncio.gather to run concurrently.
    results = []
    for c in coros:
        results.append(await c)
    return results
