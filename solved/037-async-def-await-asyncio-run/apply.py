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


async def amain(ids: list[int]) -> None:
    results = await _solo.fetch_all(ids)
    for r in results:
        print(f"id={r['id']} value={r['value']}")


def main() -> None:
    ids = [int(x) for x in sys.argv[1:]] or [1, 2, 3]
    asyncio.run(amain(ids))


if __name__ == "__main__":
    main()
