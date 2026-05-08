"""Rung 3: Guided — solved version.

`asyncio.wait_for(coro, timeout)` wraps the coroutine in a timeout
guard. On expiry it raises `asyncio.TimeoutError`. We catch that
specific exception and return the sentinel string instead of
propagating.
"""
import asyncio


async def with_timeout(coro, seconds: float):
    """Run `coro`; return its result, or "TIMED_OUT" if too slow."""
    try:
        return await asyncio.wait_for(coro, seconds)
    except asyncio.TimeoutError:
        return "TIMED_OUT"
