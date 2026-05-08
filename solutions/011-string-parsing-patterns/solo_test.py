"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.parse_env("") == {}


def test_basic():
    assert ex.parse_env("A=1\nB=2") == {"A": "1", "B": "2"}


def test_whitespace_around():
    assert ex.parse_env("  A = 1  \nB= two") == {"A": "1", "B": "two"}


def test_comment_skipped():
    assert ex.parse_env("# hi\nA=1\n  # also comment\nB=2") == {"A": "1", "B": "2"}


def test_blank_lines_skipped():
    assert ex.parse_env("A=1\n\n   \nB=2") == {"A": "1", "B": "2"}


def test_value_with_equals():
    assert ex.parse_env("URL=https://x.io/?a=b") == {"URL": "https://x.io/?a=b"}


def test_no_equals_skipped():
    assert ex.parse_env("A=1\nbroken-line\nB=2") == {"A": "1", "B": "2"}


def test_later_wins():
    assert ex.parse_env("A=1\nA=2") == {"A": "2"}
