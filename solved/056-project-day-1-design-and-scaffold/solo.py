"""Rung 4: Solo — solved version.

`snapshot_all` uses `asyncio.gather` to run all `fetch_fn(url)`
coroutines concurrently and returns results in input order. The
`fetch_fn` is injected so tests can supply a fake without httpx.
"""
import asyncio
from dataclasses import dataclass


@dataclass
class Snapshot:
    url: str
    status: int = 0
    body_length: int = 0
    error: str | None = None


async def snapshot_all(urls: list[str], fetch_fn) -> list[Snapshot]:
    return list(await asyncio.gather(*(fetch_fn(url) for url in urls)))
