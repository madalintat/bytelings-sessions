"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic(tmp_path):
    src = tmp_path / "notes.txt"
    src.write_text("hello world")
    out = ex.swap_extension(src, ".bak")
    assert out == tmp_path / "notes.bak"
    assert out.read_text() == "hello world"


def test_returns_path(tmp_path):
    src = tmp_path / "a.csv"
    src.write_text("x,y")
    out = ex.swap_extension(src, ".tsv")
    assert isinstance(out, Path)


def test_preserves_stem(tmp_path):
    src = tmp_path / "report-2026.txt"
    src.write_text("data")
    out = ex.swap_extension(src, ".md")
    assert out.stem == "report-2026"
    assert out.suffix == ".md"


def test_does_not_remove_original(tmp_path):
    src = tmp_path / "a.txt"
    src.write_text("keep me")
    ex.swap_extension(src, ".bak")
    assert src.exists()
    assert src.read_text() == "keep me"
