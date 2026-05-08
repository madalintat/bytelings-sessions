"""Rung 4: Solo — solved version.

`APage` implements the explicit async-iterator protocol:
- `__aiter__` returns `self` (the class is its own iterator).
- `__anext__` awaits a simulated network hop, then returns the next
  record by walking through the flattened pages. When the pages are
  exhausted it raises `StopAsyncIteration`.

We flatten the pages upfront during `__init__` for simplicity — the
page data is already in memory, so eagerly building a list is fine.
"""
import asyncio


class APage:
    def __init__(self, pages: list[list]) -> None:
        self._records = [record for page in pages for record in page]
        self._index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._index >= len(self._records):
            raise StopAsyncIteration
        await asyncio.sleep(0.0)
        record = self._records[self._index]
        self._index += 1
        return record
