"""Rung 4: Solo — solved version.

`gather(..., return_exceptions=True)` replaces a raised exception with
the exception *object* in the results list instead of propagating it.
We then map over the results: normal values pass through unchanged;
exception instances are converted to "ERROR: <ClassName>".
"""
import asyncio


async def fetch_all_safe(coros: list) -> list:
    raw = await asyncio.gather(*coros, return_exceptions=True)
    return [
        f"ERROR: {type(r).__name__}" if isinstance(r, BaseException) else r
        for r in raw
    ]
