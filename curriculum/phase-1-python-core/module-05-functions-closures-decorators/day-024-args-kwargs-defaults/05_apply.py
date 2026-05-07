"""Rung 5: Apply.

Tiny CLI: read tag tokens from stdin (whitespace-separated), print
each tag and its count.

Reuses tally from rung 4.

Try it: echo "a b a c b a" | uv run python 05_apply.py
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
    tokens = [t for t in sys.stdin.read().split() if not t.startswith("_")]
    counts = _solo.tally(*tokens)
    for tag in sorted(counts):
        print(f"{tag}: {counts[tag]}")


if __name__ == "__main__":
    main()
