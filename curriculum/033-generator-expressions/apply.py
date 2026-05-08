"""Rung 5: Apply.

Tiny CLI: print the lengths of the longest N lines on stdin.

Reads stdin lazily — handles huge files without blowing memory because
it pipes a generator expression through your `top_n_lengths`.

Try it:
    printf 'a\\nbb\\nccc\\ndddd\\n' | uv run python 05_apply.py 2
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    # rstrip the newline; sys.stdin is itself a lazy iterable of lines
    lines = (line.rstrip("\n") for line in sys.stdin)
    lengths = _solo.top_n_lengths(lines, n)
    for length in lengths:
        print(length)


if __name__ == "__main__":
    main()
