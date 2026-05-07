"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.strict_join("a", "b", "c") == "a b c"


def test_custom_sep():
    assert ex.strict_join("a", "b", sep="-") == "a-b"


def test_empty_default():
    assert ex.strict_join() == "(empty)"


def test_empty_custom_default():
    assert ex.strict_join(default="nothing") == "nothing"


def test_one_part():
    assert ex.strict_join("only") == "only"


def test_sep_with_one_part_returns_just_that():
    assert ex.strict_join("only", sep="--") == "only"
