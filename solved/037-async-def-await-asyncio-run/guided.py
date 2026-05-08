"""Rung 3: Guided — solved version.

`greet_after` is a coroutine: `await asyncio.sleep(delay)` suspends
it on the event loop for `delay` seconds without blocking other
coroutines, then resumes and builds the greeting string.
"""
import asyncio


async def greet_after(name: str, delay: float) -> str:
    """Sleep, then return a greeting.

    >>> import asyncio
    >>> asyncio.run(greet_after("Bytelinger", 0.0))
    'Hello, Bytelinger!'
    """
    await asyncio.sleep(delay)
    return f"Hello, {name}!"
