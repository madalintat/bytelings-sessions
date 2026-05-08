"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_folder(tmp_path):
    assert ex.largest_file(tmp_path) is None


def test_single_file(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hi")
    assert ex.largest_file(tmp_path) == p


def test_picks_largest(tmp_path):
    a = tmp_path / "small.txt"
    a.write_text("x")
    b = tmp_path / "big.txt"
    b.write_text("x" * 1000)
    c = tmp_path / "medium.txt"
    c.write_text("x" * 100)
    assert ex.largest_file(tmp_path) == b


def test_recursive(tmp_path):
    sub = tmp_path / "sub"
    sub.mkdir()
    (tmp_path / "shallow.txt").write_text("a" * 10)
    (sub / "deep.txt").write_text("a" * 100)
    assert ex.largest_file(tmp_path) == sub / "deep.txt"


def test_ignores_directories(tmp_path):
    (tmp_path / "subdir").mkdir()
    p = tmp_path / "f.txt"
    p.write_text("x")
    # The only regular file is f.txt — should be returned.
    assert ex.largest_file(tmp_path) == p
