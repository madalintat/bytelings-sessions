"""Rung 5: Apply.

Tiny CLI: read newline-separated strings, print the longest.

Try it:
    printf 'cat\\nelephant\\ndog\\n' | uv run python apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    lines = [line.rstrip("\n") for line in sys.stdin if line.strip()]
    if not lines:
        print("(no input)")
        return
    print(_solo.longest(lines))


if __name__ == "__main__":
    main()
