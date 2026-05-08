"""Rung 4: Solo — solved version.

The retry loop uses a zero-indexed attempt counter. On success we
return immediately. On any exception we compute the backoff delay
(`base_delay * 2**i`) and sleep before the next attempt. After all
attempts are exhausted we re-raise the last captured exception. Using
a factory (`fn_factory`) is necessary because coroutines are
single-use objects — each attempt needs a fresh one.
"""
import asyncio


async def retry(fn_factory, attempts: int, base_delay: float):
    last_exc: Exception | None = None
    for i in range(attempts):
        try:
            return await fn_factory()
        except Exception as exc:
            last_exc = exc
            await asyncio.sleep(base_delay * (2 ** i))
    raise last_exc
