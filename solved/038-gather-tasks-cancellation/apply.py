"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import asyncio
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


async def _ok(value):
    await asyncio.sleep(0.05)
    return value


async def _bad():
    await asyncio.sleep(0.05)
    raise RuntimeError("network down")


async def amain() -> None:
    jobs = [_ok("alpha"), _bad(), _ok("beta"), _bad(), _ok("gamma")]
    results = await _solo.fetch_all_safe(jobs)
    succeeded = sum(1 for r in results if not str(r).startswith("ERROR:"))
    failed = len(results) - succeeded
    print(f"{succeeded} ok, {failed} failed")
    for i, r in enumerate(results):
        print(f"  job {i}: {r}")


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    main()
