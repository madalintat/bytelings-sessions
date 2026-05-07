"""Day 3 tests — properties and an oracle.

The new shape: random workloads, compared against a slow-but-obviously-
correct reference implementation. If the indexed Table disagrees with
the oracle on ANY operation, we have a bug.
"""
import importlib.util
import random
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(app)


# ----------------------------------------------------------------------
#  The brute-force oracle: a list-of-rows table. Slow but obviously right.
# ----------------------------------------------------------------------
class ListTable:
    def __init__(self) -> None:
        self._next_id = 1
        self._rows: list[dict] = []

    def insert(self, range_key: int, payload: dict) -> int:
        rid = self._next_id
        self._next_id += 1
        row = {"id": rid, "range_key": range_key, **payload}
        self._rows.append(row)
        return rid

    def get(self, row_id: int):
        for r in self._rows:
            if r["id"] == row_id:
                return r
        return None

    def delete(self, row_id: int) -> bool:
        for i, r in enumerate(self._rows):
            if r["id"] == row_id:
                self._rows.pop(i)
                return True
        return False

    def range_query(self, lo: int, hi: int) -> list[dict]:
        out = [r for r in self._rows if lo <= r["range_key"] <= hi]
        out.sort(key=lambda r: (r["range_key"], r["id"]))
        return out

    def __len__(self) -> int:
        return len(self._rows)


def _normalize_range(rows):
    """Sort the rows so we can compare to the oracle (which is already sorted
    by (range_key, id))."""
    return sorted(rows, key=lambda r: (r["range_key"], r["id"]))


# ----------------------------------------------------------------------
#  Oracle property tests.
# ----------------------------------------------------------------------

def test_oracle_random_workload():
    rng = random.Random(42)
    real = app.Table()
    oracle = ListTable()
    live_ids: list[int] = []

    for step in range(500):
        op = rng.choice(["insert", "insert", "insert", "get", "delete", "range"])
        if op == "insert":
            rk = rng.randint(0, 100)
            payload = {"v": step}
            ra = real.insert(rk, payload)
            ob = oracle.insert(rk, payload)
            assert ra == ob, f"id mismatch at step {step}: real={ra} oracle={ob}"
            live_ids.append(ra)
        elif op == "get":
            rid = rng.choice(live_ids) if live_ids else 999
            assert real.get(rid) == oracle.get(rid), f"get mismatch at step {step}"
        elif op == "delete":
            if live_ids and rng.random() < 0.5:
                rid = rng.choice(live_ids)
                live_ids.remove(rid)
            else:
                rid = 99999  # guaranteed missing
            assert real.delete(rid) == oracle.delete(rid), f"delete mismatch at step {step}"
        elif op == "range":
            lo = rng.randint(0, 100)
            hi = lo + rng.randint(0, 30)
            real_rows = _normalize_range(real.range_query(lo, hi))
            oracle_rows = _normalize_range(oracle.range_query(lo, hi))
            assert real_rows == oracle_rows, (
                f"range mismatch at step {step} for [{lo},{hi}]: "
                f"real={real_rows} oracle={oracle_rows}"
            )
        assert len(real) == len(oracle), f"len mismatch at step {step}"


def test_oracle_long_run_with_many_duplicates():
    """Stress the duplicate-range_key handling."""
    rng = random.Random(7)
    real = app.Table()
    oracle = ListTable()
    for step in range(200):
        rk = rng.choice([10, 10, 20, 20, 20, 30])  # heavy duplicates
        ra = real.insert(rk, {"i": step})
        ob = oracle.insert(rk, {"i": step})
        assert ra == ob
    assert _normalize_range(real.range_query(0, 100)) == \
           _normalize_range(oracle.range_query(0, 100))


def test_inserted_rows_all_findable():
    t = app.Table()
    ids = [t.insert(i, {"i": i}) for i in range(50)]
    for rid in ids:
        assert t.get(rid) is not None


def test_range_query_returns_only_in_range():
    t = app.Table()
    for i in range(0, 100, 7):
        t.insert(i, {"i": i})
    rows = t.range_query(20, 60)
    for r in rows:
        assert 20 <= r["range_key"] <= 60


def test_len_matches_inserts_minus_deletes():
    t = app.Table()
    ids = [t.insert(i, {}) for i in range(20)]
    assert len(t) == 20
    for rid in ids[:5]:
        t.delete(rid)
    assert len(t) == 15
