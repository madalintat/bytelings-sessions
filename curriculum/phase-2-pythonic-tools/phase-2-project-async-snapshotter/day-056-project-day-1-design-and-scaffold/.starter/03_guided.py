"""Rung 3: Guided implement.

Topic: a stub `fetch` for Day 1

Implement a stub `fetch(client, url)` that returns a Snapshot:
- url: the input url
- status: 0
- body_length: 0
- error: "not implemented yet"

The stub is async and returns a Snapshot directly. Day 57 replaces
the body with a real httpx call.
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
    # TODO: return a Snapshot with the right fields.
    raise NotImplementedError
