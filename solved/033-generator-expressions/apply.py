"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. This copy is unchanged from
the starter.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    lines = (line.rstrip("\n") for line in sys.stdin)
    lengths = _solo.top_n_lengths(lines, n)
    for length in lengths:
        print(length)


if __name__ == "__main__":
    main()
