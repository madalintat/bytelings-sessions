"""Day 2 tests — the public API works end to end.

All Day 1 tests are repeated here, plus targeted tests for tricky
cases: same range_key on multiple rows, delete-and-reinsert, query
ranges that miss everything, etc.
"""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(app)


# ----- Day 1 tests, repeated -----

def test_empty_len_zero():
    assert len(app.Table()) == 0


def test_insert_returns_int():
    t = app.Table()
    rid = t.insert(30, {"name": "alice"})
    assert isinstance(rid, int)


def test_insert_then_get():
    t = app.Table()
    rid = t.insert(30, {"name": "alice"})
    row = t.get(rid)
    assert row is not None
    assert row["id"] == rid
    assert row["range_key"] == 30
    assert row["name"] == "alice"


def test_get_missing_none():
    assert app.Table().get(999) is None


def test_delete_missing_false():
    assert app.Table().delete(999) is False


def test_delete_present_true_and_removes():
    t = app.Table()
    rid = t.insert(30, {"name": "a"})
    assert t.delete(rid) is True
    assert t.get(rid) is None
    assert len(t) == 0


def test_range_empty():
    assert app.Table().range_query(0, 100) == []


def test_range_basic():
    t = app.Table()
    t.insert(20, {})
    t.insert(30, {})
    t.insert(40, {})
    assert [r["range_key"] for r in t.range_query(25, 35)] == [30]


def test_range_inclusive():
    t = app.Table()
    t.insert(20, {})
    t.insert(30, {})
    t.insert(40, {})
    assert [r["range_key"] for r in t.range_query(20, 40)] == [20, 30, 40]


# ----- Day 2 targeted tests -----

def test_duplicate_range_keys_both_visible():
    t = app.Table()
    a = t.insert(30, {"name": "a"})
    b = t.insert(30, {"name": "b"})
    rows = t.range_query(30, 30)
    names = sorted(r["name"] for r in rows)
    assert names == ["a", "b"]
    # Sanity: distinct ids despite same range_key
    assert a != b


def test_delete_one_of_duplicate_range_keys():
    t = app.Table()
    a = t.insert(30, {"name": "a"})
    b = t.insert(30, {"name": "b"})
    t.delete(a)
    rows = t.range_query(30, 30)
    assert [r["name"] for r in rows] == ["b"]
    assert t.get(a) is None
    assert t.get(b) is not None


def test_range_query_empty_intersection():
    t = app.Table()
    t.insert(10, {})
    t.insert(20, {})
    assert t.range_query(50, 100) == []


def test_range_query_negatives():
    t = app.Table()
    t.insert(-10, {"name": "n"})
    t.insert(0, {"name": "z"})
    t.insert(10, {"name": "p"})
    rows = t.range_query(-100, 0)
    assert [r["name"] for r in rows] == ["n", "z"]


def test_delete_then_reinsert_uses_new_id():
    t = app.Table()
    a = t.insert(30, {})
    t.delete(a)
    b = t.insert(30, {})
    assert b != a
    assert t.get(a) is None
    assert t.get(b) is not None


def test_indices_stay_in_sync_after_many_ops():
    t = app.Table()
    ids = [t.insert(rk, {"i": i}) for i, rk in enumerate([10, 20, 30, 40, 50])]
    # Delete the middle.
    t.delete(ids[2])
    rows = t.range_query(0, 100)
    assert [r["range_key"] for r in rows] == [10, 20, 40, 50]
    assert len(t) == 4


def test_range_query_returns_dicts_not_ids():
    t = app.Table()
    t.insert(30, {"name": "alice"})
    rows = t.range_query(20, 40)
    assert isinstance(rows[0], dict)
    assert "name" in rows[0]
