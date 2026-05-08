"""Rung 2: Fluency — solved version.

Two bugs fixed:
1. `aticks` looped with `await` but never yielded. Adding `yield i`
   makes it an async generator.
2. `collect` used plain `for` on an async generator. Async generators
   must be consumed with `async for` — the plain `for` would raise a
   TypeError at runtime.
"""
import asyncio


async def aticks(n: int):
    """Yield 0, 1, ..., n-1, with a tiny await between each."""
    for i in range(n):
        await asyncio.sleep(0.0)
        yield i


async def collect(n: int) -> list[int]:
    """Collect the first `n` ticks into a list."""
    out = []
    async for v in aticks(n):
        out.append(v)
    return out
