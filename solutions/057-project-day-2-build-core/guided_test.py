"""Tests for rung 3."""
import importlib.util
import json
from dataclasses import dataclass
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


@dataclass
class _Snap:
    url: str
    status: int = 0
    body_length: int = 0
    error: str | None = None


def test_writes_json(tmp_path):
    out = tmp_path / "snaps.json"
    snaps = [_Snap(url="http://a", status=200, body_length=5)]
    ex.save_snapshots(out, snaps)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data == [{"url": "http://a", "status": 200, "body_length": 5, "error": None}]


def test_indented(tmp_path):
    out = tmp_path / "snaps.json"
    ex.save_snapshots(out, [_Snap(url="http://a")])
    assert "\n" in out.read_text(encoding="utf-8")


def test_atomic_no_tmp_left(tmp_path):
    out = tmp_path / "snaps.json"
    ex.save_snapshots(out, [_Snap(url="http://a")])
    leftovers = list(tmp_path.glob("*.tmp"))
    assert leftovers == []


def test_uses_os_replace():
    src = (_HERE / "guided.py").read_text()
    assert "os.replace" in src, "atomic write requires os.replace"


def test_empty_list(tmp_path):
    out = tmp_path / "snaps.json"
    ex.save_snapshots(out, [])
    assert json.loads(out.read_text(encoding="utf-8")) == []
