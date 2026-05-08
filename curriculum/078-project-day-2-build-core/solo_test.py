"""HIDDEN tests for rung 4."""
import importlib.util
import logging
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE_A = (
    "2026-05-08T10:00:00 INFO path=/a status=200\n"
    "2026-05-08T10:00:01 ERROR path=/db status=500\n"
)
SAMPLE_B = (
    "2026-05-08T10:01:00 INFO path=/b status=200\n"
    "2026-05-08T10:01:01 INFO path=/a status=200\n"
)


def test_two_files_merge(tmp_path):
    a = tmp_path / "a.log"
    b = tmp_path / "b.log"
    a.write_text(SAMPLE_A)
    b.write_text(SAMPLE_B)
    agg = ex.analyze_paths([a, b])
    assert agg.parsed == 4
    assert agg.skipped == 0
    assert agg.levels == Counter({"INFO": 3, "ERROR": 1})
    assert agg.top_paths == Counter({"/a": 2, "/b": 1, "/db": 1})


def test_empty_path_list():
    agg = ex.analyze_paths([])
    assert agg.parsed == 0
    assert agg.skipped == 0


def test_missing_file_logs_warning(tmp_path, caplog):
    real = tmp_path / "real.log"
    real.write_text(SAMPLE_A)
    missing = tmp_path / "nope.log"
    with caplog.at_level(logging.WARNING, logger=ex.log.name):
        agg = ex.analyze_paths([real, missing])
    assert agg.parsed == 2
    assert any(r.levelno == logging.WARNING for r in caplog.records)
