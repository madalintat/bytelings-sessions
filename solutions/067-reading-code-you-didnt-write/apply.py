"""Rung 5: Apply.

Run `find_callers` on a real Python file, given on the command line.

Try it on this curriculum module itself:
  uv run python 05_apply.py 04_solo.py find_callers
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(f"usage: {argv[0]} <file.py> <symbol>")
        return 2
    src = Path(argv[1]).read_text()
    lines = _solo.find_callers(src, argv[2])
    if not lines:
        print(f"no calls to {argv[2]!r}")
    else:
        for ln in lines:
            print(f"{argv[1]}:{ln}: calls {argv[2]}()")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
