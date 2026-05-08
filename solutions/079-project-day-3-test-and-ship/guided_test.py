"""Tests for rung 3."""
from collections import Counter
from pathlib import Path

from _byte import load_rung

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
ex = load_rung(_HERE / "guided.py", _NAME)


SAMPLE_A = (
    "2026-05-08T10:00:00 INFO path=/a status=200\n"
    "2026-05-08T10:00:01 ERROR path=/db status=500\n"
)
SAMPLE_B = (
    "2026-05-08T10:01:00 INFO path=/b status=200\n"
    "2026-05-08T10:01:01 INFO path=/a status=200\n"
)


def test_two_files(tmp_path):
    a = tmp_path / "a.log"
    b = tmp_path / "b.log"
    a.write_text(SAMPLE_A)
    b.write_text(SAMPLE_B)
    agg = ex.analyze_paths_parallel([a, b], max_workers=2)
    assert agg.parsed == 4
    assert agg.skipped == 0
    assert agg.levels == Counter({"INFO": 3, "ERROR": 1})


def test_empty_paths():
    agg = ex.analyze_paths_parallel([])
    assert agg.parsed == 0
    assert agg.skipped == 0


def test_missing_file_silently_empty(tmp_path):
    real = tmp_path / "real.log"
    real.write_text(SAMPLE_A)
    missing = tmp_path / "nope.log"
    agg = ex.analyze_paths_parallel([real, missing], max_workers=2)
    # Real file's records still counted; missing file -> empty Aggregate merged in.
    assert agg.parsed == 2
