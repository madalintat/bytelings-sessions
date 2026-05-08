"""Rung 5: Apply.

Tiny CLI: read lines from stdin, print each unique line in first-seen order.

Reuses dedupe from rung 4.

Try it: printf "a\nb\na\nc\nb\n" | uv run python apply.py
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
    lines = [line.rstrip("\n") for line in sys.stdin]
    for line in _solo.dedupe(lines):
        print(line)


if __name__ == "__main__":
    main()
