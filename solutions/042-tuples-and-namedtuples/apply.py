"""Rung 5: Apply.

Tiny CLI: read newline-separated integers from stdin, print min/max.

Try it:
    printf '3\\n1\\n4\\n1\\n5\\n' | uv run python apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    values = [int(line) for line in sys.stdin if line.strip()]
    if not values:
        print("(no input)")
        return
    result = _solo.min_max(values)
    print(f"lo={result.lo}  hi={result.hi}  span={result.hi - result.lo}")


if __name__ == "__main__":
    main()
