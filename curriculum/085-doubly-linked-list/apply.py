"""Rung 5: Apply.

Tiny CLI: a "recently visited" tracker.

Reads urls (one per line) from stdin. For each url:
    - if it's already in the recents list, move it to the front (O(1) splice)
    - otherwise, prepend it
At the end, print the recents in order, newest first.

This is a real LRU-cache shape — minus the eviction. You'll add
eviction tomorrow on Day 86.

Try it:
    printf "a.com\\nb.com\\na.com\\nc.com\\nb.com\\n" | uv run python apply.py
    -> b.com, c.com, a.com
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
    dl = _guided.DoublyLinkedList()
    by_url: dict[str, _guided.Node] = {}

    for raw in sys.stdin:
        url = raw.strip()
        if not url:
            continue
        if url in by_url:
            node = by_url[url]
            dl.delete(node)
            new_node = dl.prepend(url)
            by_url[url] = new_node
        else:
            new_node = dl.prepend(url)
            by_url[url] = new_node

    for url in dl:
        print(url)


if __name__ == "__main__":
    main()
