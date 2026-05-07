"""Tiny in-memory database — Day 3: polished implementation + CLI.

By today, this file should be the COMPLETE Table. Copy your Day 2
implementation here and add the CLI at the bottom.

Two things to confirm:
  - len(t), get, insert, delete, range_query all work
  - the CLI in __main__ drives the table from stdin
"""
import json
import sys
from typing import Iterator, Optional


# ----------------------------------------------------------------------
#  BST keyed by (range_key, row_id) — same as Day 2.
# ----------------------------------------------------------------------
class _BSTNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class _BST:
    def __init__(self) -> None:
        self.root: Optional[_BSTNode] = None
        self._size: int = 0

    def insert(self, value) -> None:
        def _ins(n):
            if n is None:
                self._size += 1
                return _BSTNode(value)
            if value < n.value:
                n.left = _ins(n.left)
            elif value > n.value:
                n.right = _ins(n.right)
            return n
        self.root = _ins(self.root)

    def delete(self, value) -> bool:
        removed = [False]

        def _min(n):
            while n.left is not None:
                n = n.left
            return n

        def _del(n, target):
            if n is None:
                return None
            if target < n.value:
                n.left = _del(n.left, target)
            elif target > n.value:
                n.right = _del(n.right, target)
            else:
                removed[0] = True
                if n.left is None:
                    return n.right
                if n.right is None:
                    return n.left
                succ = _min(n.right)
                n.value = succ.value
                n.right = _del(n.right, succ.value)
            return n

        self.root = _del(self.root, value)
        if removed[0]:
            self._size -= 1
        return removed[0]

    def range_scan(self, lo_key, hi_key) -> Iterator:
        """Yield (range_key, row_id) tuples whose range_key in [lo_key, hi_key]."""
        def walk(n):
            if n is None:
                return
            rk, _ = n.value
            if rk > lo_key:
                yield from walk(n.left)
            if lo_key <= rk <= hi_key:
                yield n.value
            if rk < hi_key:
                yield from walk(n.right)
        yield from walk(self.root)

    def __len__(self) -> int:
        return self._size


# ----------------------------------------------------------------------
#  The Table.
# ----------------------------------------------------------------------
class Table:
    """In-memory table with hash + range indices.

    By Day 3 this should be the implementation that passes everything.
    The body below is intentionally LEFT UNFINISHED so the day's tests
    stay informative — copy your Day 2 solution here.
    """

    def __init__(self) -> None:
        self._next_id: int = 1
        self._by_id: dict[int, dict] = {}
        self._by_range: _BST = _BST()

    def insert(self, range_key: int, payload: dict) -> int:
        # TODO: copy your Day 2 implementation.
        raise NotImplementedError

    def get(self, row_id: int) -> Optional[dict]:
        # TODO: copy your Day 2 implementation.
        raise NotImplementedError

    def delete(self, row_id: int) -> bool:
        # TODO: copy your Day 2 implementation.
        raise NotImplementedError

    def range_query(self, lo: int, hi: int) -> list[dict]:
        # TODO: copy your Day 2 implementation.
        # Tip: today you can use self._by_range.range_scan(lo, hi)
        # for a tighter walk that prunes irrelevant subtrees.
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self._by_id)


# ----------------------------------------------------------------------
#  The CLI.
# ----------------------------------------------------------------------
def _cli() -> None:
    """Drive the table from stdin.

    Commands:
        insert <range_key> <json_payload>
        get <id>
        delete <id>
        range <lo> <hi>
        len
        quit
    """
    t = Table()
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        if line == "quit":
            return
        parts = line.split(maxsplit=2)
        try:
            if parts[0] == "insert" and len(parts) == 3:
                rk = int(parts[1])
                payload = json.loads(parts[2])
                rid = t.insert(rk, payload)
                print(rid)
            elif parts[0] == "get" and len(parts) == 2:
                row = t.get(int(parts[1]))
                print(json.dumps(row) if row is not None else "null")
            elif parts[0] == "delete" and len(parts) == 2:
                print(t.delete(int(parts[1])))
            elif parts[0] == "range" and len(parts) == 3:
                _, lo, hi = parts[0], int(parts[1]), int(parts[2])
                rows = t.range_query(lo, hi)
                for r in rows:
                    print(json.dumps(r))
            elif parts[0] == "len":
                print(len(t))
            else:
                print(f"unknown: {line!r}", file=sys.stderr)
        except (ValueError, json.JSONDecodeError) as e:
            print(f"error: {e}", file=sys.stderr)


if __name__ == "__main__":
    _cli()
