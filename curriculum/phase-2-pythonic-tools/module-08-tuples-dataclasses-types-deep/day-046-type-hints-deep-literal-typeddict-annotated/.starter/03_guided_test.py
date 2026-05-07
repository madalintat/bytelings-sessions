"""Tests for rung 3."""
import importlib.util
import typing
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_a():
    assert ex.classify(95) == "A"
    assert ex.classify(90) == "A"


def test_b():
    assert ex.classify(89) == "B"
    assert ex.classify(70) == "B"


def test_c():
    assert ex.classify(69) == "C"
    assert ex.classify(50) == "C"


def test_f():
    assert ex.classify(49) == "F"
    assert ex.classify(0) == "F"


def test_grade_is_literal():
    args = typing.get_args(ex.Grade)
    assert set(args) == {"A", "B", "C", "F"}
