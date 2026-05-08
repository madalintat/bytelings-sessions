"""Rung 2: Fluency — solved version.

Two bugs fixed:
1. `double` was a plain `def`. Tests call `await double(n)`, which
   requires a coroutine. Adding `async` makes it one.
2. `add_after_delay` called `asyncio.sleep(delay)` without `await`.
   Without `await` the coroutine object is created but never run —
   the function returns immediately, ignoring the delay.
"""
import asyncio


async def double(n: int) -> int:
    """Return 2 * n."""
    return 2 * n


async def add_after_delay(a: int, b: int, delay: float) -> int:
    """Wait `delay` seconds, then return a + b."""
    await asyncio.sleep(delay)
    return a + b
