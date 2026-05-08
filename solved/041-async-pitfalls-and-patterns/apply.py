"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import asyncio
import random
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


_attempts = {"n": 0}


async def flaky_service() -> str:
    _attempts["n"] += 1
    await asyncio.sleep(0.01)
    if random.random() < 0.6:
        raise RuntimeError("transient")
    return f"OK (succeeded on attempt {_attempts['n']})"


async def amain() -> None:
    random.seed(0)
    try:
        result = await _solo.retry(flaky_service, attempts=8, base_delay=0.0)
        print(result)
    except Exception as e:
        print(f"gave up: {e}")


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    main()
