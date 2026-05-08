"""Rung 2: Fluency drill — fix the two async functions.

Topic: async def, await, asyncio.run

Both functions below have a bug. Fix them.
"""
import asyncio


def double(n: int) -> int:
    """Return 2 * n. The tests use `await double(n)`, so this must be async."""
    # TODO: make this an async function (one keyword on the def line).
    return 2 * n


async def add_after_delay(a: int, b: int, delay: float) -> int:
    """Wait `delay` seconds, then return a + b."""
    # TODO: this calls asyncio.sleep but never awaits it. Add the missing keyword.
    asyncio.sleep(delay)
    return a + b
