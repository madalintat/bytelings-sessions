"""Rung 3: Guided implement.

Topic: bounded concurrency with a Semaphore

Implement `bounded_fetch(coros, max_in_flight)`:
- Run all coroutines, but never more than `max_in_flight` at the same
  time.
- Return the list of results in input order.

Use an `asyncio.Semaphore(max_in_flight)`. Wrap each coroutine in a
helper that does `async with sem:` before awaiting it, then gather.
"""
import asyncio


async def bounded_fetch(coros: list, max_in_flight: int) -> list:
    """Run `coros` concurrently with at most `max_in_flight` running together."""
    # TODO: Semaphore + helper + gather.
    raise NotImplementedError
