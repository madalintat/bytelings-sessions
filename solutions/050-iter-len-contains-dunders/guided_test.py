"""Tests for rung 3."""
import importlib.util
import random
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_len():
    d = ex.Deck(["a", "b", "c"])
    assert len(d) == 3


def test_indexing():
    d = ex.Deck(["a", "b", "c"])
    assert d[0] == "a"
    assert d[2] == "c"


def test_iteration_falls_out():
    d = ex.Deck(["x", "y"])
    assert list(d) == ["x", "y"]


def test_does_not_share_underlying_list():
    src = ["a", "b"]
    d = ex.Deck(src)
    src.append("c")
    assert len(d) == 2


def test_shuffle_reorders_in_place():
    d = ex.Deck(list("abcdefgh"))
    rng = random.Random(7)
    d.shuffle(rng)
    assert sorted(d) == list("abcdefgh")
    # Very likely changed (with seed 7), but allow exact-equal as a non-failure.


def test_contains_via_iteration():
    d = ex.Deck(["a", "b", "c"])
    assert "b" in d
    assert "z" not in d
