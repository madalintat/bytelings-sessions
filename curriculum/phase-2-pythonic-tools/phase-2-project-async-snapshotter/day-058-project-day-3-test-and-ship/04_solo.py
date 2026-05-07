"""Rung 4: Day 3 checkpoint — the shippable build.

Topic: bring it all together

Provide:

1. `Snapshot` dataclass: url, status, body_length, error.

2. async `fetch(client, url) -> Snapshot`:
   - GET with timeout=5.0
   - status + body_length on success (any HTTP code)
   - On httpx.HTTPError: status=0, body_length=0, error=type(e).__name__

3. async `snapshot_all(client, urls, max_in_flight=20) -> list[Snapshot]`:
   - Fetch all URLs concurrently, capped at `max_in_flight`.
   - Returns Snapshots in input order.

4. sync `save_snapshots(path, snapshots)`:
   - Atomic JSON write, indent=2, sort_keys=True, encoding utf-8.

Today's behavior is the union of Days 56 and 57, plus the bounded
concurrency. (We're keeping retry separate as a stretch — the test
focuses on what's required.)

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
    client: httpx.AsyncClient, urls: list[str], max_in_flight: int = 20
) -> list[Snapshot]:
    raise NotImplementedError


def save_snapshots(path: Path, snapshots: list[Snapshot]) -> None:
    raise NotImplementedError
