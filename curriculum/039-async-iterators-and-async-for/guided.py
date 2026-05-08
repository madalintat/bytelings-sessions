"""Rung 3: Guided implement.

Topic: async generator that filters another async source

Implement `aeven(source)` — an async generator that yields only the
even numbers from `source` (which is itself an async iterable).

>>> # used like:
>>> async def main():
...     async for v in aeven(some_async_source()):
...         print(v)
"""
import asyncio


async def aeven(source):
    """Yield items from `source` whose value is even.

    `source` is async-iterable (you must use `async for`).
    """
    # TODO: async for x in source: if x % 2 == 0: yield x
    raise NotImplementedError
