"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.sort_by_length(["bee", "a", "carrot"]) == ["a", "bee", "carrot"]


def test_descending():
    assert ex.sort_by_length(["bee", "a", "carrot"], descending=True) == [
        "carrot", "bee", "a"
    ]


def test_stable_ties():
    # All length 2 — original order preserved (sorted is stable)
    assert ex.sort_by_length(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]


def test_empty():
    assert ex.sort_by_length([]) == []


def test_single():
    assert ex.sort_by_length(["only"]) == ["only"]


def test_does_not_mutate():
    src = ["bee", "a", "carrot"]
    ex.sort_by_length(src)
    assert src == ["bee", "a", "carrot"]
