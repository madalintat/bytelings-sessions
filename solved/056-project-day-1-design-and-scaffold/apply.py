"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import asyncio
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


async def stub_fetch(url: str) -> "_solo.Snapshot":
    """Day 1 stand-in for a real fetch. Returns a fake-success snapshot."""
    await asyncio.sleep(0.01)
    return _solo.Snapshot(url=url, status=200, body_length=len(url))


async def amain(urls: list[str]) -> None:
    snapshots = await _solo.snapshot_all(urls, stub_fetch)
    for s in snapshots:
        marker = "OK " if s.error is None else "ERR"
        print(f"{marker} {s.status:>3}  {s.body_length:>5}b  {s.url}")


def main() -> None:
    urls = sys.argv[1:] or ["http://a", "http://b", "http://c"]
    asyncio.run(amain(urls))


if __name__ == "__main__":
    main()
