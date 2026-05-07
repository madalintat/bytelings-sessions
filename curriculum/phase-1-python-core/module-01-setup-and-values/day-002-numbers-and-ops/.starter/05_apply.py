"""Rung 5 — find the smallest number whose digits sum to a target.

For input N, print the smallest non-negative integer x such that
digit_sum(x) == N.

Try: uv run python 05_apply.py 15
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: 05_apply.py TARGET")
        return
    target = int(sys.argv[1])
    x = 0
    while _solo.digit_sum(x) != target:
        x += 1
    print(x)


if __name__ == "__main__":
    main()
