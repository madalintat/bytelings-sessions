"""Rung 3: Guided — solved version.

We create one coroutine per URL with `client.get(url)`, then
`gather` all of them. `zip(urls, responses)` pairs each original
URL with its response, preserving input order — gather guarantees
output order matches input order.
"""
import asyncio

import httpx


async def fetch_many(
    client: httpx.AsyncClient, urls: list[str]
) -> list[tuple[str, int]]:
    """Concurrent GETs. Returns [(url, status_code), ...] in input order."""
    responses = await asyncio.gather(*(client.get(url) for url in urls))
    return [(url, resp.status_code) for url, resp in zip(urls, responses)]
