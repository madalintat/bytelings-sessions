"""Rung 3: Guided implement.

Topic: asyncio.wait_for + cancellation

Implement `with_timeout(coro, seconds)`:
- Run the coroutine.
- If it finishes within `seconds`, return its result.
- If it doesn't, return the string "TIMED_OUT" instead of raising.

Use `asyncio.wait_for`. It raises `asyncio.TimeoutError` (alias of
TimeoutError on 3.11+) when the deadline hits.
"""
import asyncio


async def with_timeout(coro, seconds: float):
    """Run `coro`; return its result, or "TIMED_OUT" if too slow."""
    # TODO: try/except around await asyncio.wait_for(coro, seconds).
    raise NotImplementedError
