"""Rung 5: Apply.

Tiny CLI: read words (whitespace-separated) from stdin, print the
most common one.

Reuses most_common from rung 4.

Try it: echo "the quick brown fox the lazy dog the" | uv run python apply.py
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
    words = sys.stdin.read().split()
    if not words:
        print("(no input)")
        return
    print(_solo.most_common(words))


if __name__ == "__main__":
    main()
