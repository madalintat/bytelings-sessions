"""Rung 2: Fluency drill — fix the status checker.

Topic: httpx.AsyncClient + async with

`check_status(client, url)` should fetch `url` and return the status
code. Fix the missing await + the wrong context-manager flavor.
"""
import httpx


async def check_status(client: httpx.AsyncClient, url: str) -> int:
    """Return the integer HTTP status code for `url`."""
    # TODO: missing `await` — this returns a coroutine, not a Response.
    response = client.get(url)
    return response.status_code


async def open_client_and_check(url: str) -> int:
    """Open an httpx AsyncClient, check the URL, return the status code."""
    # TODO: this uses `with`, but AsyncClient needs `async with`.
    with httpx.AsyncClient() as client:
        return await check_status(client, url)
