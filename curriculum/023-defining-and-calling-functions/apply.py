"""Rung 5: Apply.

Tiny CLI: parse its own argv via parse_flags from rung 4, then echo
the parsed config dict.

Reuses parse_flags from rung 4.

Try it: uv run python apply.py --verbose --out=hello.txt --count 3
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
    try:
        cfg = _solo.parse_flags(sys.argv[1:])
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)
    for key in ("verbose", "out", "count"):
        print(f"{key}: {cfg[key]!r}")


if __name__ == "__main__":
    main()
