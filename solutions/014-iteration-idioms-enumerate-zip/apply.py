"""Rung 5: Apply.

Tiny CLI: read numbers from stdin (one per line), print running diffs.

Reuses running_diffs from rung 4.

Try it: printf "10\n12\n9\n14\n" | uv run python apply.py

Patterns: P-13 (enumerate-for-index), P-14 (zip-parallel-walk), P-15 (unpacking-into-named).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    nums = [float(line) for line in sys.stdin if line.strip()]
    diffs = _solo.running_diffs(nums)
    for d in diffs:
        print(d)


if __name__ == "__main__":
    main()
