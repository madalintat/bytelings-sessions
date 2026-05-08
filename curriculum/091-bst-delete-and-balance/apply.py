"""Rung 5: Apply.

Tiny CLI: load a stream of integers, build a BST, then report whether
it's healthy or skewed.

Reads one integer per line from stdin. After EOF, prints:
    size, height, ideal_height, skewed?

Try it:
    seq 1 100 | uv run python apply.py
    -> size=100 height=99 ideal=6 skewed=True

    seq 1 100 | shuf | uv run python apply.py    # randomized order
    -> size=100 height=10..15 (varies) ideal=6 skewed=False (probably)
"""
import math
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)


def main() -> None:
    t = _guided.BST()
    for raw in sys.stdin:
        s = raw.strip()
        if not s:
            continue
        try:
            t.insert(int(s))
        except ValueError:
            print(f"skipping non-integer: {s!r}", file=sys.stderr)
    n = len(t)
    h = t.height()
    ideal = -1 if n == 0 else math.floor(math.log2(n))
    print(f"size={n} height={h} ideal={ideal} skewed={t.is_skewed()}")


if __name__ == "__main__":
    main()
