"""Rung 5: Apply.

Tiny CLI: tail the last N lines from stdin, then echo them.

Try it:
    seq 1 100 | uv run python 05_apply.py 5
    -> last five lines: 96..100
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "03_guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    lines = (line.rstrip("\n") for line in sys.stdin)
    tail = _guided.last_n(lines, n)
    for line in tail:
        print(line)


if __name__ == "__main__":
    main()
