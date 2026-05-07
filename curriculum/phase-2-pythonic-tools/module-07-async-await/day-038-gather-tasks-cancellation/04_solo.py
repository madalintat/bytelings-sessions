"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: gather with error tolerance

Implement `fetch_all_safe(coros)`:
- `coros` is a list of awaitables.
- Run all of them concurrently.
- For each, if it returns a value, keep that value.
- For each, if it raises an exception, replace with the string
  "ERROR: <ExceptionClassName>" (e.g. "ERROR: ValueError").
- Return the list of values/strings, in the same order as the inputs.

Hint: `asyncio.gather` accepts a `return_exceptions=True` kwarg that
makes it return the exception instance instead of raising.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import asyncio


async def fetch_all_safe(coros: list) -> list:
    raise NotImplementedError
