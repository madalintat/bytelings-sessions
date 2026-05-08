"""Rung 3: Guided — solved version.

A `Semaphore(max_in_flight)` acts as a counter-gate: at most
`max_in_flight` coroutines can hold the semaphore simultaneously.
We wrap each coroutine in `_guarded` that acquires the semaphore
before running the actual work, then release it on exit. `gather`
starts all the wrappers; the semaphore naturally serialises them in
batches.
"""
import asyncio


async def bounded_fetch(coros: list, max_in_flight: int) -> list:
    """Run `coros` concurrently with at most `max_in_flight` running together."""
    sem = asyncio.Semaphore(max_in_flight)

    async def _guarded(coro):
        async with sem:
            return await coro

    return list(await asyncio.gather(*(_guarded(c) for c in coros)))
