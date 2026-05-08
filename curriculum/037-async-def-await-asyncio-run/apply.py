"""Rung 5: Apply.

Tiny CLI: fetch a few fake items by id and print them.

Try it:
    uv run python apply.py 1 2 3
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
