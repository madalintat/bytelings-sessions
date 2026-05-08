"""Rung 3: Guided implement.

Topic: an async function that calls another async function

Implement `greet_after(name, delay)`:
- Wait `delay` seconds (use `asyncio.sleep`).
- Then return f"Hello, {name}!".

Both `name` and `delay` come in as arguments. The function must be a
coroutine (defined with `async def`).
"""
import asyncio


async def greet_after(name: str, delay: float) -> str:
    """Sleep, then return a greeting.

    >>> import asyncio
    >>> asyncio.run(greet_after("Bytelinger", 0.0))
    'Hello, Bytelinger!'
    """
    # TODO: await asyncio.sleep(delay) and then return the formatted string.
    raise NotImplementedError
