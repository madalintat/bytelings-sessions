"""Rung 3: Guided — solved version.

We retry up to `attempts` times. 4xx `HTTPStatusError` is a client
error (e.g. Not Found) — retrying won't help, so we re-raise
immediately. Any other exception is transient and we retry. After all
attempts fail, we re-raise the last exception.
"""
import asyncio

import httpx


async def with_retries(coro_factory, attempts: int):
    last_exc: Exception | None = None
    for _ in range(attempts):
        try:
            return await coro_factory()
        except Exception as exc:
            if isinstance(exc, httpx.HTTPStatusError) and 400 <= exc.response.status_code < 500:
                raise
            last_exc = exc
    raise last_exc
