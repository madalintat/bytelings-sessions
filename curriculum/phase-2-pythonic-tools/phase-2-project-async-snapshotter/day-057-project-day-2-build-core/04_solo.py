"""Rung 4: Day 2 checkpoint.

Topic: end-to-end snapshot pipeline

Provide:

1. The `Snapshot` dataclass (same fields as Day 1).

2. An async `fetch(client, url) -> Snapshot` that:
   - GETs the url with timeout=5.0
   - On success: status + body_length from the response
   - On any httpx.HTTPError: status=0, body_length=0, error=type(e).__name__

3. An async `snapshot_all(client, urls) -> list[Snapshot]` that fetches
   every URL concurrently using `client` and returns Snapshots in
   input order.

4. A sync `save_snapshots(path, snapshots)` that writes the list as
   JSON, indented + sorted keys, atomically (utf-8 encoding).

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
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
    raise NotImplementedError


async def snapshot_all(
    client: httpx.AsyncClient, urls: list[str]
) -> list[Snapshot]:
    raise NotImplementedError


def save_snapshots(path: Path, snapshots: list[Snapshot]) -> None:
    raise NotImplementedError
