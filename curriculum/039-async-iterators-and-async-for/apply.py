"""Rung 5: Apply.

Tiny CLI: simulate paginated fetching by streaming an APage and
printing one record at a time.

Try it:
    uv run python apply.py
"""
import asyncio
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


async def amain() -> None:
    pages = [
        [{"id": 1, "name": "alpha"}, {"id": 2, "name": "beta"}],
        [{"id": 3, "name": "gamma"}],
        [{"id": 4, "name": "delta"}, {"id": 5, "name": "epsilon"}],
    ]
    stream = _solo.APage(pages)
    async for record in stream:
        print(f"  {record['id']:>3}  {record['name']}")


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    main()
