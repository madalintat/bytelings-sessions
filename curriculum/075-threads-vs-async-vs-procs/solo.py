"""Rung 4: Solo implement.

Topic: a small async port.

asyncio is its own world; today is just the smallest taste.

Implement `async_gather_lengths(urls, fetcher)`:
  - Async function (use `async def`).
  - `fetcher` is an ASYNC function: `async def fetcher(url) -> str`.
  - Use `asyncio.gather` to run all `fetcher(url)` calls concurrently.
  - Return a list of `len(result)` IN INPUT ORDER.

Plus:
  Implement `run_sync(urls, fetcher) -> list[int]`:
  - A regular sync function that wraps the async one with `asyncio.run`.

Hidden tests in 04_solo_test.py.
"""
import asyncio
from typing import Awaitable, Callable


async def async_gather_lengths(
    urls: list[str],
    fetcher: Callable[[str], Awaitable[str]],
) -> list[int]:
    raise NotImplementedError


def run_sync(
    urls: list[str],
    fetcher: Callable[[str], Awaitable[str]],
) -> list[int]:
    raise NotImplementedError
