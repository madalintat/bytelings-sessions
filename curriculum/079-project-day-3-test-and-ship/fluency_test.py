"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE = "\n".join(
    f"2026-05-08T10:00:{i:02d} INFO path=/api/{i % 5} status=200"
    for i in range(1000)
)


def test_returns_list_of_strings():
    out = ex.top_hotspots(SAMPLE, 3)
    assert isinstance(out, list)
    assert all(isinstance(s, str) for s in out)
    assert len(out) <= 3


def test_finds_user_functions():
    """parse_line is the per-line workhorse — it should appear in the top hotspots."""
    out = ex.top_hotspots(SAMPLE, 10)
    assert any("parse_line" in s or "analyze_text" in s for s in out), (
        f"expected parse_line / analyze_text in hotspots, got {out}"
    )


def test_excludes_builtins():
    out = ex.top_hotspots(SAMPLE, 20)
    for name in out:
        assert not name.startswith("<"), f"built-in leaked into output: {name!r}"
