"""Rung 5: Apply.

Tiny CLI: read 'KEY=VALUE' lines from stdin, print 'VALUE=KEY'.

Reuses invert from rung 4.

Try it: printf "a=1\nb=2\nc=1\n" | uv run python 05_apply.py
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
    pairs = {}
    for line in sys.stdin:
        line = line.strip()
        if "=" not in line:
            continue
        k, _, v = line.partition("=")
        pairs[k.strip()] = v.strip()
    inverted = _solo.invert(pairs)
    for k, v in inverted.items():
        print(f"{k}={v}")


if __name__ == "__main__":
    main()
