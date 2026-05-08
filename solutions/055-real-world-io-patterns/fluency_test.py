"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_writes_text(tmp_path):
    p = tmp_path / "report.txt"
    ex.save_report(p, "hello")
    assert p.read_text(encoding="utf-8") == "hello"


def test_overwrites(tmp_path):
    p = tmp_path / "report.txt"
    p.write_text("old")
    ex.save_report(p, "new")
    assert p.read_text(encoding="utf-8") == "new"


def test_handles_non_ascii(tmp_path):
    """Without encoding='utf-8', writing emoji on some platforms breaks."""
    p = tmp_path / "report.txt"
    ex.save_report(p, "café — ☕")
    assert p.read_bytes() == "café — ☕".encode("utf-8")


def test_uses_atomic_write(tmp_path):
    """Source must use os.replace for atomicity."""
    src = (_HERE / "fluency.py").read_text()
    assert "os.replace" in src, (
        "use os.replace(tmp, path) to make the write atomic"
    )


def test_no_tmp_left_on_success(tmp_path):
    p = tmp_path / "out.txt"
    ex.save_report(p, "ok")
    assert p.exists()
    # The .tmp sibling must be gone (renamed atomically into place).
    assert not (tmp_path / "out.txt.tmp").exists()
