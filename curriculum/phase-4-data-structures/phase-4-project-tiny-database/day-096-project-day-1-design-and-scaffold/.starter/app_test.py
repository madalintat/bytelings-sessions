"""Day 1 tests — interface only.

These tests exercise the public API shape WITHOUT implementing it.
On Day 1 most will fail (raising NotImplementedError); that's
expected and informative — you're seeing what work is left.
"""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_app"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "app.py")
app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(app)


def test_empty_table_has_length_zero():
    t = app.Table()
    assert len(t) == 0


def test_insert_returns_int_id():
    """insert returns an int. The first id is documented as 1."""
    t = app.Table()
    rid = t.insert(30, {"name": "alice"})
    assert isinstance(rid, int)
    assert rid == 1


def test_insert_then_get_returns_row():
    t = app.Table()
    rid = t.insert(30, {"name": "alice"})
    row = t.get(rid)
    assert row is not None
    assert row["id"] == rid
    assert row["range_key"] == 30
    assert row["name"] == "alice"


def test_get_missing_returns_none():
    t = app.Table()
    assert t.get(999) is None


def test_delete_missing_returns_false():
    t = app.Table()
    assert t.delete(999) is False


def test_delete_present_returns_true_and_removes():
    t = app.Table()
    rid = t.insert(30, {"name": "alice"})
    assert t.delete(rid) is True
    assert t.get(rid) is None
    assert len(t) == 0


def test_range_query_on_empty_table():
    t = app.Table()
    assert t.range_query(0, 100) == []


def test_range_query_basic():
    t = app.Table()
    t.insert(20, {"name": "a"})
    t.insert(30, {"name": "b"})
    t.insert(40, {"name": "c"})
    out = t.range_query(25, 35)
    assert len(out) == 1
    assert out[0]["name"] == "b"


def test_range_query_inclusive_bounds():
    t = app.Table()
    t.insert(20, {"name": "a"})
    t.insert(30, {"name": "b"})
    t.insert(40, {"name": "c"})
    out = t.range_query(20, 40)
    names = [r["name"] for r in out]
    assert sorted(names) == ["a", "b", "c"]


def test_range_query_sorted_ascending():
    t = app.Table()
    t.insert(50, {"name": "x"})
    t.insert(10, {"name": "y"})
    t.insert(30, {"name": "z"})
    out = t.range_query(0, 100)
    assert [r["range_key"] for r in out] == [10, 30, 50]


def test_two_inserts_get_unique_ids():
    t = app.Table()
    a = t.insert(10, {"name": "a"})
    b = t.insert(20, {"name": "b"})
    assert a != b


def test_len_grows_and_shrinks():
    t = app.Table()
    a = t.insert(10, {})
    b = t.insert(20, {})
    assert len(t) == 2
    t.delete(a)
    assert len(t) == 1
    t.delete(b)
    assert len(t) == 0
