"""Rung 5: Apply.

Tiny CLI: read integers, one per line, from stdin and print the top K
largest in descending order. The whole stream might be larger than
memory — but the heap only holds K at a time.

Try it:
    seq 1 1000000 | shuf | uv run python 05_apply.py 5
    -> 1000000
       999999
       999998
       999997
       999996
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
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    def stream():
        for raw in sys.stdin:
            s = raw.strip()
            if not s:
                continue
            try:
                yield int(s)
            except ValueError:
                continue

    for v in _solo.top_k(stream(), k):
        print(v)


if __name__ == "__main__":
    main()
