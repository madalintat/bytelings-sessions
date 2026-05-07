"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: retries with exponential backoff

Implement `retry(fn_factory, attempts, base_delay)`:
- `fn_factory` is a *callable* that, when called with no args, returns
  a fresh awaitable (a coroutine). It's a factory because a coroutine
  is single-use; you need a new one per attempt.
- Try the awaitable up to `attempts` times.
- If it returns a value, return that value.
- If it raises, await `asyncio.sleep(base_delay * (2 ** i))` where `i`
  is the zero-indexed attempt number, then try again.
- If all attempts fail, re-raise the last exception.

Example:
    counter = {"n": 0}
    async def flaky():
        counter["n"] += 1
        if counter["n"] < 3:
            raise RuntimeError("nope")
        return "ok"
    result = asyncio.run(retry(flaky, 5, 0.0))   # "ok"

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import asyncio


async def retry(fn_factory, attempts: int, base_delay: float):
    raise NotImplementedError
