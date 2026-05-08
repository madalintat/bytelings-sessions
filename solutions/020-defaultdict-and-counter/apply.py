"""Rung 5: Apply.

Tiny CLI: read two strings (lines via stdin), print the letter diff
sorted by char.

Reuses letter_diff from rung 4.

Try it: printf "hello\nworld\n" | uv run python 05_apply.py
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
    lines = [line.rstrip("\n") for line in sys.stdin]
    if len(lines) < 2:
        print("need 2 lines on stdin", file=sys.stderr)
        sys.exit(2)
    a, b = lines[0], lines[1]
    diff = _solo.letter_diff(a, b)
    for char in sorted(diff):
        sign = "+" if diff[char] > 0 else ""
        print(f"{char!r}: {sign}{diff[char]}")


if __name__ == "__main__":
    main()
