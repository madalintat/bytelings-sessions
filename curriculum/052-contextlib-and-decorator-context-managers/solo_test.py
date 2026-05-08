"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_paths(tmp_path):
    assert ex.read_all_lines([]) == []


def test_single_file(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("alpha\nbeta\n")
    assert ex.read_all_lines([str(p)]) == ["alpha", "beta"]


def test_multi_file_order(tmp_path):
    a = tmp_path / "a.txt"
    a.write_text("a1\na2\n")
    b = tmp_path / "b.txt"
    b.write_text("b1\n")
    assert ex.read_all_lines([str(a), str(b)]) == ["a1", "a2", "b1"]


def test_strips_trailing_newline(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hello\n")
    out = ex.read_all_lines([str(p)])
    assert out == ["hello"]
    assert all("\n" not in line for line in out)


def test_uses_exitstack():
    """The function must reference ExitStack, not be a recursive nested-with."""
    src = (_HERE / "04_solo.py").read_text()
    assert "ExitStack" in src, "use contextlib.ExitStack to manage many files"


def test_propagates_open_failure(tmp_path):
    a = tmp_path / "a.txt"
    a.write_text("ok\n")
    bogus = tmp_path / "does-not-exist.txt"
    with pytest.raises(FileNotFoundError):
        ex.read_all_lines([str(a), str(bogus)])
