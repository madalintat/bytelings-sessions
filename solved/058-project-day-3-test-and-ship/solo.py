"""Rung 4: Solo — solved version.

The shippable build combines Day 56 + Day 57 plus bounded concurrency.
`snapshot_all` uses a `Semaphore(max_in_flight)` guard around each
fetch so the number of simultaneous requests is capped.
"""
import asyncio
import dataclasses
import json
import os
from dataclasses import dataclass
from pathlib import Path

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


async def snapshot_all(
    client: httpx.AsyncClient, urls: list[str], max_in_flight: int = 20
) -> list[Snapshot]:
    sem = asyncio.Semaphore(max_in_flight)

    async def _guarded(url: str) -> Snapshot:
        async with sem:
            return await fetch(client, url)

    return list(await asyncio.gather(*(_guarded(u) for u in urls)))


def save_snapshots(path: Path, snapshots: list[Snapshot]) -> None:
    payload = [dataclasses.asdict(s) for s in snapshots]
    text = json.dumps(payload, indent=2, sort_keys=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)
