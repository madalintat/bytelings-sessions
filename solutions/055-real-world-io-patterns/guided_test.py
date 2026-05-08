"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic(tmp_path):
    p = tmp_path / "log.txt"
    p.write_text("error: x\nok\nerror: y\nfine\nerror: z\n", encoding="utf-8")
    assert ex.count_matching_lines(p, "error") == 3


def test_no_match(tmp_path):
    p = tmp_path / "log.txt"
    p.write_text("ok\nfine\n", encoding="utf-8")
    assert ex.count_matching_lines(p, "missing") == 0


def test_empty_file(tmp_path):
    p = tmp_path / "log.txt"
    p.write_text("", encoding="utf-8")
    assert ex.count_matching_lines(p, "anything") == 0


def test_uses_streaming():
    """Source must NOT read the whole file at once via read_text/splitlines."""
    src = (_HERE / "guided.py").read_text()
    assert "splitlines" not in src
    assert "read_text" not in src


def test_explicit_encoding():
    """Source must specify encoding='utf-8'."""
    src = (_HERE / "guided.py").read_text()
    assert 'encoding="utf-8"' in src or "encoding='utf-8'" in src
