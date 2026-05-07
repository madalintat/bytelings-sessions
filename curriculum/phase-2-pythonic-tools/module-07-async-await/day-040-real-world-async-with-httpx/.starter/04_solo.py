"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a tiny health-check tool

Implement `health_report(client, urls)`:
- Run all GETs concurrently using `client`.
- For each URL, classify the result:
    - 200..299 → "ok"
    - other status code → "bad"
    - any exception (timeout, network error, etc.) → "error"
- Return a dict mapping url → classification string.

Hint: wrap each per-url coroutine so a raised exception turns into the
sentinel "error" instead of crashing gather.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import asyncio

import httpx


async def health_report(
    client: httpx.AsyncClient, urls: list[str]
) -> dict[str, str]:
    raise NotImplementedError
