"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
import json
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _double_n(d):
    return {**d, "n": d["n"] * 2}


def test_basic(tmp_path):
    src = tmp_path / "in.jsonl"
    src.write_text('{"n": 1}\n{"n": 2}\n{"n": 3}\n', encoding="utf-8")
    dst = tmp_path / "out.jsonl"
    written = ex.transform_jsonl(src, dst, _double_n)
    assert written == 3
    out_lines = dst.read_text(encoding="utf-8").splitlines()
    assert [json.loads(line) for line in out_lines] == [
        {"n": 2}, {"n": 4}, {"n": 6}
    ]


def test_skips_bad_lines(tmp_path):
    src = tmp_path / "in.jsonl"
    src.write_text('{"n": 1}\nNOT JSON\n{"n": 2}\n', encoding="utf-8")
    dst = tmp_path / "out.jsonl"
    written = ex.transform_jsonl(src, dst, _double_n)
    assert written == 2


def test_empty_input(tmp_path):
    src = tmp_path / "in.jsonl"
    src.write_text("", encoding="utf-8")
    dst = tmp_path / "out.jsonl"
    written = ex.transform_jsonl(src, dst, _double_n)
    assert written == 0
    assert dst.exists()


def test_atomic_no_tmp_left(tmp_path):
    src = tmp_path / "in.jsonl"
    src.write_text('{"n": 1}\n', encoding="utf-8")
    dst = tmp_path / "out.jsonl"
    ex.transform_jsonl(src, dst, _double_n)
    # No leftover .tmp sibling.
    leftovers = list(tmp_path.glob("*.tmp"))
    assert leftovers == [], f"unexpected temp files: {leftovers}"


def test_uses_atomic_write():
    src = (_HERE / "solo.py").read_text()
    assert "os.replace" in src, "atomic write requires os.replace"


def test_unicode_roundtrip(tmp_path):
    src = tmp_path / "in.jsonl"
    src.write_text('{"name": "café"}\n{"name": "東京"}\n', encoding="utf-8")
    dst = tmp_path / "out.jsonl"
    ex.transform_jsonl(src, dst, lambda d: d)
    out = [json.loads(line) for line in dst.read_text(encoding="utf-8").splitlines()]
    assert out == [{"name": "café"}, {"name": "東京"}]
