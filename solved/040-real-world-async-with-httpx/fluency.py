"""Rung 2: Fluency — solved version.

Two bugs fixed:
1. `check_status` called `client.get(url)` without `await`. httpx's
   async client returns a coroutine; without `await` `response` is the
   coroutine object, not the Response.
2. `open_client_and_check` used plain `with` for `httpx.AsyncClient`.
   AsyncClient is an async context manager and requires `async with`.
"""
import httpx


async def check_status(client: httpx.AsyncClient, url: str) -> int:
    """Return the integer HTTP status code for `url`."""
    response = await client.get(url)
    return response.status_code


async def open_client_and_check(url: str) -> int:
    """Open an httpx AsyncClient, check the URL, return the status code."""
    async with httpx.AsyncClient() as client:
        return await check_status(client, url)
