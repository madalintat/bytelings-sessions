"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic(tmp_path):
    p = tmp_path / "users.csv"
    p.write_text("id,name\n1,Mada\n2,Alex\n")
    assert ex.load_users(p) == [
        {"id": 1, "name": "Mada"},
        {"id": 2, "name": "Alex"},
    ]


def test_id_is_int(tmp_path):
    p = tmp_path / "users.csv"
    p.write_text("id,name\n42,Bob\n")
    rows = ex.load_users(p)
    assert isinstance(rows[0]["id"], int)


def test_skips_bad_rows(tmp_path):
    p = tmp_path / "users.csv"
    p.write_text("id,name\n1,Good\nNOT_INT,Bad\n2,Also_Good\n")
    rows = ex.load_users(p)
    assert rows == [
        {"id": 1, "name": "Good"},
        {"id": 2, "name": "Also_Good"},
    ]


def test_empty_csv(tmp_path):
    p = tmp_path / "users.csv"
    p.write_text("id,name\n")
    assert ex.load_users(p) == []
