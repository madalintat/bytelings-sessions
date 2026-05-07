"""Rung 5: Apply.

Tiny CLI: build a step-pattern by repeating a small set of values.

Reads two args: a comma-separated list of strings, and a repeat count.
Prints them concatenated.

Try it:
    uv run python 05_apply.py "tick,tock" 3
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: 05_apply.py <a,b,c> <count>")
        return
    values = sys.argv[1].split(",")
    times = int(sys.argv[2])
    pattern = _solo.Repeat(values, times)
    print(" ".join(pattern))


if __name__ == "__main__":
    main()
