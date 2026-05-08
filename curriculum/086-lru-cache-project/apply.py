"""Rung 5: Apply.

Tiny CLI: an LRU-backed key/value store driven by stdin.

Commands:
    put <key> <value>
    get <key>
    show          (newest -> oldest)
    quit

Try it:
    printf "put a 1\\nput b 2\\nget a\\nput c 3\\nshow\\nquit\\n" \\
        | uv run python 05_apply.py 2
    -> 1
       a=1, c=3
    (b was evicted because get(a) made b the LRU)
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "03_guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)


def _items_newest_first(c: "_guided.LRUCache"):
    cur = c.head.next
    while cur is not c.tail:
        yield cur.key, cur.value
        cur = cur.next


def main() -> None:
    capacity = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    cache = _guided.LRUCache(capacity)
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if not line:
            continue
        if line == "quit":
            return
        parts = line.split(maxsplit=2)
        if parts[0] == "put" and len(parts) == 3:
            cache.put(parts[1], parts[2])
        elif parts[0] == "get" and len(parts) == 2:
            v = cache.get(parts[1])
            print("(miss)" if v is None else v)
        elif parts[0] == "show":
            print(", ".join(f"{k}={v}" for k, v in _items_newest_first(cache)))
        else:
            print(f"unknown: {line!r}")


if __name__ == "__main__":
    main()
