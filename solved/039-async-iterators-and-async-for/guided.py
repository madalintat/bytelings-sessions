"""Rung 3: Guided — solved version.

`aeven` is an async generator: it consumes `source` with `async for`
and re-yields only even values. The `async for` is necessary because
`source` is an async iterable; plain `for` would raise TypeError.
"""
import asyncio


async def aeven(source):
    """Yield items from `source` whose value is even."""
    async for x in source:
        if x % 2 == 0:
            yield x
