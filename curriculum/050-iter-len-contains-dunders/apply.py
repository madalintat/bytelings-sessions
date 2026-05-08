"""Rung 5: Apply.

Tiny CLI: read lines from stdin, print them in order with duplicates
stripped (insertion-order, like a unique-but-ordered list).

Try it:
    printf 'b\\na\\nb\\nc\\na\\n' | uv run python 05_apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    seen = _solo.OrderedSet()
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if line:
            seen.add(line)
    print(f"({len(seen)} unique)")
    for line in seen:
        print(line)


if __name__ == "__main__":
    main()
