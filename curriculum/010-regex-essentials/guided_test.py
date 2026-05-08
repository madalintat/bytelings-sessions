"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.parse_log_line("2026-05-08 14:33:21 ERROR boom") == (
        "2026-05-08", "14:33:21", "ERROR", "boom"
    )


def test_message_with_spaces():
    assert ex.parse_log_line("2026-05-08 14:33:21 INFO hello world") == (
        "2026-05-08", "14:33:21", "INFO", "hello world"
    )


def test_all_levels():
    for lvl in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        line = f"2026-01-01 00:00:00 {lvl} x"
        assert ex.parse_log_line(line) == ("2026-01-01", "00:00:00", lvl, "x")


def test_no_match_returns_none():
    assert ex.parse_log_line("nope") is None
    assert ex.parse_log_line("") is None


def test_invalid_level_no_match():
    assert ex.parse_log_line("2026-05-08 14:33:21 TRACE something") is None


def test_invalid_date_format_no_match():
    assert ex.parse_log_line("2026/05/08 14:33:21 INFO x") is None
