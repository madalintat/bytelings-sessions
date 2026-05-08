"""Rung 5: Apply.

Tiny CLI: read "Last, First" lines from stdin, print "First Last".

Reuses flip_name from rung 4.

Try it: printf "Smith, John\nDoe, Jane\nalice\n" | uv run python 05_apply.py
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
    for line in sys.stdin:
        line = line.rstrip("\n")
        flipped = _solo.flip_name(line)
        if flipped:
            print(flipped)


if __name__ == "__main__":
    main()
