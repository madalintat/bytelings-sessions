"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_parse_basic():
    assert ex.parse_entry_point("habit_cli.cli:main") == ("habit_cli.cli", "main")


def test_parse_top_level():
    assert ex.parse_entry_point("tool:run") == ("tool", "run")


def test_valid_basic():
    assert ex.is_valid_entry_point("habit_cli.cli:main") is True


def test_invalid_no_colon():
    assert ex.is_valid_entry_point("habit_cli.main") is False


def test_invalid_too_many_colons():
    assert ex.is_valid_entry_point("a:b:c") is False


def test_invalid_empty_sides():
    assert ex.is_valid_entry_point(":main") is False
    assert ex.is_valid_entry_point("habit_cli:") is False
    assert ex.is_valid_entry_point(":") is False
