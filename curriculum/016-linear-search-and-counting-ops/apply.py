"""Rung 5: Apply.

Tiny CLI: read integers from stdin, take TARGET from argv, print the
pair indices (or 'no pair').

Reuses find_pair_with_sum from rung 4.

Try it: printf "1\n2\n3\n4\n" | uv run python 05_apply.py 5
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
        print("usage: 05_apply.py <target>", file=sys.stderr)
        sys.exit(2)
    target = int(sys.argv[1])
    nums = [int(line) for line in sys.stdin if line.strip()]
    pair = _solo.find_pair_with_sum(nums, target)
    if pair is None:
        print("no pair")
    else:
        i, j = pair
        print(f"{i},{j} -> {nums[i]} + {nums[j]} = {target}")


if __name__ == "__main__":
    main()
