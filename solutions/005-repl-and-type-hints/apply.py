"""Rung 5 — given a list of integers from stdin (one per line), print the mean.

Try: printf "1\\n2\\n3\\n4\\n" | uv run python 05_apply.py
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
    nums = [float(line) for line in sys.stdin if line.strip()]
    print(_solo.mean(nums))


if __name__ == "__main__":
    main()
