"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_equality():
    assert ex.Tag("python") == ex.Tag("python")


def test_inequality():
    assert ex.Tag("python") != ex.Tag("rust")


def test_hashable():
    s = {ex.Tag("python"), ex.Tag("python"), ex.Tag("rust")}
    assert len(s) == 2


def test_dict_key_lookup():
    d = {ex.Tag("python"): "great"}
    assert d[ex.Tag("python")] == "great"


def test_hashes_match_when_equal():
    a = ex.Tag("x")
    b = ex.Tag("x")
    assert a == b
    assert hash(a) == hash(b)
