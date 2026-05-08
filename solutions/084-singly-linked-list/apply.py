"""Rung 5: Apply.

Tiny CLI: read lines from stdin, prepend each to a linked list (so the
oldest ends up last), then print the list — which gives you a "newest
first" feed.

This isn't strictly a linked-list-only problem, but it's a plausible
real shape: a chat feed where the most recent message goes on top, and
prepend is the natural operation. With a linked list, that's O(1).

Try it:
    printf "hi\\nhello\\nyo\\n" | uv run python apply.py
    -> yo
       hello
       hi
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
    feed = _guided.LinkedList()
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if not line:
            continue
        feed.prepend(line)
    for msg in feed:
        print(msg)


if __name__ == "__main__":
    main()
