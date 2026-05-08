"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import asyncio
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import httpx

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def _demo_handler(request):
    p = request.url.path
    if p.startswith("/ok"):
        return httpx.Response(200, text="hello")
    if p.startswith("/big"):
        return httpx.Response(200, text="x" * 4096)
    if p.startswith("/missing"):
        return httpx.Response(404, text="nope")
    if p.startswith("/boom"):
        raise httpx.ConnectError("offline", request=request)
    return httpx.Response(500)


def _demo_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        transport=httpx.MockTransport(_demo_handler),
        base_url="http://demo",
    )


URLS = [
    "http://demo/ok",
    "http://demo/big",
    "http://demo/missing",
    "http://demo/boom",
]


async def amain(out: Path) -> None:
    async with _demo_client() as client:
        snapshots = await _solo.snapshot_all(client, URLS)
    _solo.save_snapshots(out, snapshots)
    for s in snapshots:
        marker = "OK " if s.error is None else "ERR"
        print(f"{marker} {s.status:>3}  {s.body_length:>6}b  {s.url}")
    print(f"wrote {len(snapshots)} records to {out}")


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/snaps.json")
    asyncio.run(amain(out))


if __name__ == "__main__":
    main()
