"""Rung 4: Day 1 checkpoint — implement `snapshot_all`.

Topic: tying the pieces together

Implement two things:

1. The `Snapshot` dataclass (same as rungs 2 + 3): fields url, status,
   body_length, error, with the same defaults.

2. An async function `snapshot_all(urls, fetch_fn)`:
   - `urls` is a list of strings.
   - `fetch_fn` is an async callable (url, ) -> Snapshot. (We pass it
     in so tests can inject a fake; tomorrow's app.py wires in the
     real httpx-backed one.)
   - Build coroutines for every URL by calling `fetch_fn(url)`.
   - Run them concurrently with asyncio.gather.
   - Return the list of Snapshots in input order.

Constraints:
- No httpx today. The fake fetch_fn does whatever the test wants.
- snapshot_all must NOT crash if fetch_fn returns a Snapshot whose
  error field is set — just include it in the list as-is.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
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
    raise NotImplementedError
