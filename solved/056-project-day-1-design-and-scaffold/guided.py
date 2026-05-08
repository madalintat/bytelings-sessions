"""Rung 3: Guided — solved version.

The stub `fetch` is an `async def` that returns a `Snapshot` with
`error="not implemented yet"` and all other fields at their defaults.
Day 57 replaces this body with a real httpx call.
"""
from dataclasses import dataclass


@dataclass
class Snapshot:
    url: str
    status: int = 0
    body_length: int = 0
    error: str | None = None


async def fetch(client, url: str) -> Snapshot:
    """Stub for Day 1. Day 57 will wire this up to httpx.AsyncClient."""
    return Snapshot(url=url, error="not implemented yet")
