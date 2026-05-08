"""Rung 5: Apply.

Tiny CLI: print the first N natural numbers whose square is < limit.

Demonstrates `naturals()` (infinite) piped into `take_while` (bails out
when squares get too big). Lazy all the way through.

Try it:
    uv run python apply.py 100
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    small_squares = _solo.take_while(lambda n: n * n < limit, _solo.naturals())
    for n in small_squares:
        print(f"{n}^2 = {n * n}")


if __name__ == "__main__":
    main()
