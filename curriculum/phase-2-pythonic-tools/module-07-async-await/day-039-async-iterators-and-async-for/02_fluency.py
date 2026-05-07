"""Rung 2: Fluency drill — fix the async generator + its consumer.

Topic: async generators and async for
"""
import asyncio


async def aticks(n: int):
    """Yield 0, 1, ..., n-1, with a tiny await between each."""
    for i in range(n):
        await asyncio.sleep(0.0)
        # TODO: missing the actual yield — add one that produces `i`.
        pass


async def collect(n: int) -> list[int]:
    """Collect the first `n` ticks into a list."""
    out = []
    # TODO: use `async for` (not plain `for`) to iterate aticks.
    for v in aticks(n):
        out.append(v)
    return out
