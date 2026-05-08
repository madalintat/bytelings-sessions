"""Rung 3: Guided implement.

Topic: fan out N HTTP GETs concurrently with one client

Implement `fetch_many(client, urls)`:
- For each URL, GET it via `client.get(url)`.
- Run all the GETs concurrently with asyncio.gather.
- Return a list of (url, status_code) tuples in the same order as
  `urls`.

The caller passes in an already-built httpx.AsyncClient — don't make
your own. (The tests will inject a MockTransport client.)
"""
import asyncio

import httpx


async def fetch_many(
    client: httpx.AsyncClient, urls: list[str]
) -> list[tuple[str, int]]:
    """Concurrent GETs. Returns [(url, status_code), ...] in input order."""
    # TODO: build a coroutine per URL, gather them, zip with input order.
    raise NotImplementedError
