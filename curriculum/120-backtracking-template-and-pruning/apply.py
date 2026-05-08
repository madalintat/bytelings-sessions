"""Rung 5: Apply.

Mini lottery-pick generator: print all 6-of-49 combinations? No, that's
14 million. Print only the COUNT — and a small example: all 3-of-7
combinations.

Try it: uv run python apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    combos = _solo.combinations(7, 3)
    print(f"All 3-of-7 combinations ({len(combos)} total):")
    for c in combos:
        print(f"  {c}")


if __name__ == "__main__":
    main()
