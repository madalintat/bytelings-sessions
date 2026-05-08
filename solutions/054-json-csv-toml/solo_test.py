"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
import json
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic(tmp_path):
    toml_path = tmp_path / "in.toml"
    toml_path.write_text('name = "swe-skills"\nversion = "0.0.1"\n')
    json_path = tmp_path / "out.json"
    result = ex.toml_to_json(toml_path, json_path)
    assert result == {"name": "swe-skills", "version": "0.0.1"}


def test_writes_pretty_json(tmp_path):
    toml_path = tmp_path / "in.toml"
    toml_path.write_text('a = 1\nb = 2\n')
    json_path = tmp_path / "out.json"
    ex.toml_to_json(toml_path, json_path)
    text = json_path.read_text()
    # Pretty-printed JSON has newlines.
    assert "\n" in text


def test_sorted_keys(tmp_path):
    toml_path = tmp_path / "in.toml"
    toml_path.write_text('zebra = 1\napple = 2\nmango = 3\n')
    json_path = tmp_path / "out.json"
    ex.toml_to_json(toml_path, json_path)
    text = json_path.read_text()
    # 'apple' should appear before 'zebra' if sort_keys=True.
    assert text.index("apple") < text.index("zebra")


def test_nested_table(tmp_path):
    toml_path = tmp_path / "in.toml"
    toml_path.write_text('[project]\nname = "x"\nversion = "1"\n')
    json_path = tmp_path / "out.json"
    result = ex.toml_to_json(toml_path, json_path)
    assert result == {"project": {"name": "x", "version": "1"}}
    # round-trip via the JSON file too
    assert json.loads(json_path.read_text()) == {"project": {"name": "x", "version": "1"}}


def test_returns_dict(tmp_path):
    toml_path = tmp_path / "in.toml"
    toml_path.write_text('x = 1\n')
    json_path = tmp_path / "out.json"
    result = ex.toml_to_json(toml_path, json_path)
    assert isinstance(result, dict)
