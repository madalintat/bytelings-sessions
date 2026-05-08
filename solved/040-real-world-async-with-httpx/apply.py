"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import asyncio
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import httpx

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def _handler(request):
    path = request.url.path
    if path == "/auth":
        return httpx.Response(200)
    if path == "/billing":
        return httpx.Response(500)
    if path == "/search":
        raise httpx.ConnectError("offline", request=request)
    return httpx.Response(404)


URLS = [
    "http://demo/auth",
    "http://demo/billing",
    "http://demo/search",
    "http://demo/missing",
]


async def amain() -> None:
    transport = httpx.MockTransport(_handler)
    async with httpx.AsyncClient(transport=transport) as client:
        report = await _solo.health_report(client, URLS)
    for url in URLS:
        status = report[url]
        marker = {"ok": "OK", "bad": "BAD", "error": "ERR"}[status]
        print(f"{marker:<5} {url}")


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    main()
