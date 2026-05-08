"""Day 102 — Project Day 3: final Table + CLI.

Same implementation as Day 101. The oracle property tests in
app_test.py compare this Table against a naive ListTable on 500
random operations.

CLI usage (if __name__ == "__main__"):
  > insert 30 {"name": "alice"}
  > get 1
  > range 0 100
  > quit
"""
import bisect
import json
import sys
from typing import Optional


class Table:
    """Tiny in-memory database table with hash + range indices."""

    def __init__(self) -> None:
        self._by_id: dict[int, dict] = {}
        self._by_range: list[tuple] = []
        self._next_id: int = 1

    def insert(self, range_key: int, payload: dict) -> int:
        row_id = self._next_id
        self._next_id += 1
        row = {"id": row_id, "range_key": range_key, **payload}
        self._by_id[row_id] = row
        bisect.insort(self._by_range, (range_key, row_id))
        return row_id

    def get(self, row_id: int) -> Optional[dict]:
        return self._by_id.get(row_id)

    def delete(self, row_id: int) -> bool:
        row = self._by_id.pop(row_id, None)
        if row is None:
            return False
        key = (row["range_key"], row_id)
        idx = bisect.bisect_left(self._by_range, key)
        if idx < len(self._by_range) and self._by_range[idx] == key:
            del self._by_range[idx]
        return True

    def range_query(self, lo: int, hi: int) -> list[dict]:
        lo_idx = bisect.bisect_left(self._by_range, (lo, -1))
        hi_idx = bisect.bisect_right(self._by_range, (hi, float("inf")))
        result = []
        for rk, rid in self._by_range[lo_idx:hi_idx]:
            row = self._by_id.get(rid)
            if row is not None:
                result.append(row)
        return result

    def __len__(self) -> int:
        return len(self._by_id)


def _run_cli(table: Table) -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line or line == "quit":
            break
        parts = line.split(None, 2)
        cmd = parts[0]
        if cmd == "insert" and len(parts) >= 3:
            rk = int(parts[1])
            payload = json.loads(parts[2])
            print(table.insert(rk, payload))
        elif cmd == "get" and len(parts) >= 2:
            row = table.get(int(parts[1]))
            print(json.dumps(row) if row else "null")
        elif cmd == "range" and len(parts) >= 3:
            lo, hi = int(parts[1]), int(parts[2])
            for row in table.range_query(lo, hi):
                print(json.dumps(row))
        elif cmd == "delete" and len(parts) >= 2:
            print(table.delete(int(parts[1])))
        else:
            print(f"unknown command: {line!r}", file=sys.stderr)


if __name__ == "__main__":
    _run_cli(Table())
