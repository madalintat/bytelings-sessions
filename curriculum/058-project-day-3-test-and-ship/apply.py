"""Rung 5: Day 3 — the shippable CLI (app.py).

Snapshotter v1.0.

Reads URLs from a file (one per line), fetches them concurrently with
a configurable cap, writes a JSON report.

Try it (with the bundled offline demo):
    printf 'http://demo/ok\\nhttp://demo/big\\nhttp://demo/missing\\n' > /tmp/urls.txt
    uv run python apply.py /tmp/urls.txt --out /tmp/snaps.json --concurrency 5
"""
import argparse
import asyncio
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import httpx

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def _demo_handler(request):
    p = request.url.path
    if p.startswith("/ok"):
        return httpx.Response(200, text="hi")
    if p.startswith("/big"):
        return httpx.Response(200, text="x" * 4096)
    if p.startswith("/missing"):
        return httpx.Response(404)
    if p.startswith("/boom"):
        raise httpx.ConnectError("offline", request=request)
    return httpx.Response(500)


def _make_client(use_demo: bool) -> httpx.AsyncClient:
    if use_demo:
        return httpx.AsyncClient(
            transport=httpx.MockTransport(_demo_handler),
            base_url="http://demo",
        )
    return httpx.AsyncClient()


async def amain(urls: list[str], out: Path, concurrency: int, use_demo: bool) -> None:
    async with _make_client(use_demo) as client:
        snapshots = await _solo.snapshot_all(client, urls, max_in_flight=concurrency)
    _solo.save_snapshots(out, snapshots)
    ok = sum(1 for s in snapshots if s.error is None)
    print(f"{ok}/{len(snapshots)} ok  →  {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch URLs concurrently.")
    parser.add_argument("urls_file", type=Path, help="One URL per line")
    parser.add_argument("--out", type=Path, default=Path("snapshots.json"),
                        help="Output JSON path")
    parser.add_argument("--concurrency", type=int, default=20,
                        help="Max concurrent fetches")
    parser.add_argument("--demo", action="store_true",
                        help="Use offline mock client (any http://demo/* URL)")
    args = parser.parse_args()

    urls = [
        line.strip()
        for line in args.urls_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    asyncio.run(amain(urls, args.out, args.concurrency, args.demo))


if __name__ == "__main__":
    main()
