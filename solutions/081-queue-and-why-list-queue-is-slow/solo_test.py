"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_returns_none():
    assert ex.first_unique_char("") is None


def test_single_char():
    assert ex.first_unique_char("z") == "z"


def test_basic():
    assert ex.first_unique_char("aabbc") == "c"


def test_all_repeat_returns_none():
    assert ex.first_unique_char("aabb") is None


def test_first_match_wins():
    assert ex.first_unique_char("abacabad") == "c"


def test_unique_at_front():
    assert ex.first_unique_char("xyyzz") == "x"
