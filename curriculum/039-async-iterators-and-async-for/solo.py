"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: implement an async iterator class

Build `APage(pages)` — an async iterable backed by a list of "pages",
where each page is a list. Iterating an `APage` should yield every
record from every page in order, simulating a paginated API.

Constraints:
- Implement `__aiter__` and `__anext__` (the explicit class form).
- Each `__anext__` must `await asyncio.sleep(0.0)` once before
  returning a record (simulates a network hop).
- When all records are exhausted, `__anext__` must raise
  `StopAsyncIteration`.
- The class must support `async for`.

Example:
    p = APage([[1, 2], [3], [4, 5]])
    async for r in p: print(r)        # 1, 2, 3, 4, 5

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import asyncio


class APage:
    def __init__(self, pages: list[list]) -> None:
        raise NotImplementedError
