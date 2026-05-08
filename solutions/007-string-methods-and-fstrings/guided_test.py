"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.make_display_name("alice") == "Alice"


def test_strips_and_capitalizes():
    assert ex.make_display_name("  alice   wonderland ") == "Alice Wonderland"


def test_empty():
    assert ex.make_display_name("") == "(anonymous)"


def test_only_whitespace():
    assert ex.make_display_name("   ") == "(anonymous)"


def test_truncates():
    out = ex.make_display_name("alpha bravo charlie delta", max_len=15)
    assert out == "Alpha Bravo Ch…"
    assert len(out) == 15


def test_no_truncate_at_boundary():
    out = ex.make_display_name("alice wonderland", max_len=20)
    assert out == "Alice Wonderland"


def test_lowercases_all_caps_input():
    assert ex.make_display_name("BOB SMITH") == "Bob Smith"
