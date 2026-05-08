"""Rung 5: Apply.

Tiny CLI: read "task<TAB>priority" lines from stdin, print them in
priority order (lowest priority value first, FIFO on ties).

Try it:
    printf "send-email\\t2\\nbackup\\t1\\nrender-report\\t2\\n" \\
        | uv run python apply.py
    -> backup
       send-email
       render-report
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)


def main() -> None:
    pq = _guided.PriorityQueue()
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if not line:
            continue
        if "\t" not in line:
            print(f"skipping (no tab): {line!r}", file=sys.stderr)
            continue
        item, prio = line.rsplit("\t", 1)
        try:
            pq.push(item, int(prio))
        except ValueError:
            print(f"bad priority: {prio!r}", file=sys.stderr)
    while pq:
        print(pq.pop())


if __name__ == "__main__":
    main()
