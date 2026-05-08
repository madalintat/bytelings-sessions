"""Rung 5: Apply.

Tiny CLI: a "seen-before?" deduplicator.

Reads lines from stdin. For each line:
    - if it's already been seen, skip it
    - otherwise, print it and remember it

Try it:
    printf "a\\nb\\na\\nc\\nb\\nd\\n" | uv run python apply.py
    -> a
       b
       c
       d
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
    seen = _solo.HashSet()
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if line in seen:
            continue
        seen.add(line)
        print(line)


if __name__ == "__main__":
    main()
