"""Rung 2: Fluency drill — make this concurrent.

Topic: asyncio.gather

`fetch_all` currently awaits each fetch one-by-one. Rewrite it so the
fetches run concurrently. Use asyncio.gather. Order of results must
match order of inputs.
"""
import asyncio


async def _slow_double(n: int) -> int:
    await asyncio.sleep(0.05)
    return n * 2


async def fetch_all(ns: list[int]) -> list[int]:
    """Return [n*2 for n in ns], with all calls concurrent."""
    # TODO: replace this sequential loop with a single gather call.
    results = []
    for n in ns:
        results.append(await _slow_double(n))
    return results
