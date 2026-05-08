"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    rs = [
        {"name": "a", "team": "red"},
        {"name": "b", "team": "blue"},
        {"name": "c", "team": "red"},
    ]
    out = ex.index_by(rs, "team")
    assert out == {
        "red": [{"name": "a", "team": "red"}, {"name": "c", "team": "red"}],
        "blue": [{"name": "b", "team": "blue"}],
    }


def test_empty():
    assert ex.index_by([], "team") == {}


def test_skip_missing_key():
    rs = [{"team": "x"}, {"no_team": 1}, {"team": "x"}]
    out = ex.index_by(rs, "team")
    assert out == {"x": [{"team": "x"}, {"team": "x"}]}


def test_returns_plain_dict():
    """Should NOT be a defaultdict — accessing missing keys must raise KeyError."""
    out = ex.index_by([{"team": "a"}], "team")
    assert type(out) is dict


def test_preserves_order_within_group():
    rs = [{"k": "g", "n": 1}, {"k": "g", "n": 2}, {"k": "g", "n": 3}]
    out = ex.index_by(rs, "k")
    assert [r["n"] for r in out["g"]] == [1, 2, 3]
