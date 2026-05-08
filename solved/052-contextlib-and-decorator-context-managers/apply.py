"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    paths = sys.argv[1:]
    if not paths:
        print("usage: apply.py <file> [<file> ...]")
        return
    try:
        lines = _solo.read_all_lines(paths)
    except FileNotFoundError as e:
        print(f"error: {e}")
        return
    print(f"({len(lines)} lines from {len(paths)} files)")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
