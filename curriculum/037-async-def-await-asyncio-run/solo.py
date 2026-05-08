"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: write a tiny async pipeline

Implement two coroutines:

1. `fake_fetch(item_id)` — pretends to be a network call.
   - `await asyncio.sleep(0.01)` once
   - return `{"id": item_id, "value": item_id * 10}`

2. `fetch_all(ids)` — given a list of ints, await `fake_fetch` for each
   one IN SEQUENCE and return the list of results in the same order.

Note: this is the SLOW way (sequential await). Day 38 makes it fast
with gather. For now, focus on getting the calls + awaits right.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import asyncio


async def fake_fetch(item_id: int) -> dict:
    raise NotImplementedError


async def fetch_all(ids: list[int]) -> list[dict]:
    raise NotImplementedError
