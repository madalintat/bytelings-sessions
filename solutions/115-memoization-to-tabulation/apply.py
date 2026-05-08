"""Rung 5: Apply.

A tiny "elevation cost" planner. Read a small triangle of altitudes
and print the cheapest descent.

Try it: uv run python apply.py

Patterns: P-28 (memoize-recursive).
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
    print("Altitude triangle:")
    for row in triangle:
        print(" ".join(f"{x:>2}" for x in row).center(15))
    print(f"\nCheapest descent total: {_solo.min_path(triangle)}")


if __name__ == "__main__":
    main()
