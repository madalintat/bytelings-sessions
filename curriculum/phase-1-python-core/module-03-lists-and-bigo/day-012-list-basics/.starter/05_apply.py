"""Rung 5: Apply.

Tiny CLI: read lines from stdin and print them rotated by N (first arg).

Reuses rotate from rung 4.

Try it: printf "a\nb\nc\nd\n" | uv run python 05_apply.py 2
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
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    lines = [line.rstrip("\n") for line in sys.stdin]
    for line in _solo.rotate(lines, k):
        print(line)


if __name__ == "__main__":
    main()
