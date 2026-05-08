"""Rung 3: Guided implement.

Topic: retry transient HTTP failures

Implement `with_retries(coro_factory, attempts)`:
- `coro_factory()` returns a fresh awaitable on each call.
- Try up to `attempts` times.
- If the awaitable returns a value, return it (success).
- If the awaitable raises, retry — UNLESS:
    - It's an httpx.HTTPStatusError with response.status_code 4xx, in
      which case don't retry; re-raise immediately.
- If all attempts fail, re-raise the last exception.

Hint: catch `Exception`, then check if it's an httpx.HTTPStatusError
with a 4xx code and re-raise without retrying.
"""
import asyncio

import httpx


async def with_retries(coro_factory, attempts: int):
    # TODO: loop attempts; on success return; on 4xx re-raise;
    # otherwise keep last exception and re-raise after final failure.
    raise NotImplementedError
