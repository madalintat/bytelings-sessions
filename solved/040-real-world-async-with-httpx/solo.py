"""Rung 4: Solo — solved version.

We wrap each GET in a helper that catches all exceptions and maps the
result to "ok", "bad", or "error". `gather` then runs all helpers
concurrently. Using `return_exceptions=False` (the default) is fine
because the helper itself never raises — errors become strings.
"""
import asyncio

import httpx


async def health_report(
    client: httpx.AsyncClient, urls: list[str]
) -> dict[str, str]:
    async def _check(url: str) -> tuple[str, str]:
        try:
            resp = await client.get(url)
            status = "ok" if 200 <= resp.status_code < 300 else "bad"
        except Exception:
            status = "error"
        return url, status

    pairs = await asyncio.gather(*(_check(u) for u in urls))
    return dict(pairs)
