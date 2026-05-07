"""Tests for rung 2."""
import importlib.util
import json
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_load_basic(tmp_path):
    p = tmp_path / "config.json"
    p.write_text('{"name": "Mada", "n": 7}')
    assert ex.load_config(p) == {"name": "Mada", "n": 7}


def test_save_and_load_roundtrip(tmp_path):
    p = tmp_path / "out.json"
    data = {"x": 1, "y": [1, 2, 3]}
    ex.save_config(p, data)
    assert ex.load_config(p) == data


def test_save_writes_indented(tmp_path):
    p = tmp_path / "out.json"
    ex.save_config(p, {"a": 1, "b": 2})
    text = p.read_text()
    assert "\n" in text, "save_config must write indented JSON"


def test_load_does_not_use_eval():
    """eval is unsafe on untrusted JSON. Source must use json.loads / json.load."""
    src = (_HERE / "02_fluency.py").read_text()
    assert "eval(" not in src, "use json.loads, not eval"
