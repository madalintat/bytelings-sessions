"""Tests for rung 3."""
import importlib.util
import logging
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


GOOD = (
    "2026-05-08T10:00:00 INFO path=/users status=200\n"
    "2026-05-08T10:00:01 INFO path=/users status=200\n"
    "2026-05-08T10:00:02 ERROR path=/db status=500\n"
)


def test_basic_counts():
    agg = ex.analyze_text(GOOD)
    assert agg.parsed == 3
    assert agg.skipped == 0
    assert agg.levels == Counter({"INFO": 2, "ERROR": 1})
    assert agg.top_paths == Counter({"/users": 2, "/db": 1})


def test_skips_malformed():
    text = GOOD + "garbage line\n"
    agg = ex.analyze_text(text)
    assert agg.parsed == 3
    assert agg.skipped == 1


def test_skips_empty_lines():
    text = "\n\n" + GOOD + "\n"
    agg = ex.analyze_text(text)
    assert agg.parsed == 3
    # 3 blank lines -> 3 skipped
    assert agg.skipped == 3


def test_does_not_propagate_malformed(caplog):
    """log.debug message goes out at DEBUG; analyze_text returns normally."""
    with caplog.at_level(logging.DEBUG, logger=ex.log.name):
        ex.analyze_text("definitely not a log line")
    # Found at least one debug-level skip message.
    assert any(r.levelno == logging.DEBUG for r in caplog.records)


def test_no_path_field_skipped_in_top_paths():
    text = "2026-05-08T10:00:00 INFO status=200\n"
    agg = ex.analyze_text(text)
    assert agg.parsed == 1
    assert agg.top_paths == Counter()
