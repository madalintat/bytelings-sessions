"""Rung 2: Fluency drill — fix `fetch` to use the real httpx client.

Topic: project core, Day 2

`fetch` should:
1. await client.get(url, timeout=5.0)
2. Build a Snapshot with status and body_length from the response.
3. On any httpx.HTTPError, return a Snapshot with status=0,
   body_length=0, error=type(e).__name__.

The current body is stub-shaped. Wire up the real call.
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
    # TODO: replace this stub with a real httpx GET wrapped in try/except.
    return Snapshot(url=url, error="not implemented yet")
