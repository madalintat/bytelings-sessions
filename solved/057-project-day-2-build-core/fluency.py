"""Rung 2: Fluency — solved version.

`fetch` awaits `client.get(url, timeout=5.0)`. On success it
populates `status` and `body_length` from the response. The
`except httpx.HTTPError` clause catches all httpx network/HTTP errors
and stores the exception class name as `error`.
"""
from dataclasses import dataclass

import httpx


@dataclass
class Snapshot:
    url: str
    status: int = 0
    body_length: int = 0
    error: str | None = None


async def fetch(client: httpx.AsyncClient, url: str) -> Snapshot:
    try:
        response = await client.get(url, timeout=5.0)
        return Snapshot(
            url=url,
            status=response.status_code,
            body_length=len(response.content),
        )
    except httpx.HTTPError as e:
        return Snapshot(url=url, error=type(e).__name__)
