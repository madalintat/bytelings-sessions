"""Rung 5: Apply.

Tiny ATM dispenser: given a target amount, print the fewest coins
to dispense from a fixed set.

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


COINS_RON = [1, 5, 10, 50, 100, 500]


def main() -> None:
    for amount in [3, 17, 63, 248, 1234]:
        n = _solo.min_coins(COINS_RON, amount)
        print(f"  {amount:>5} bani: {n} coins")


if __name__ == "__main__":
    main()
