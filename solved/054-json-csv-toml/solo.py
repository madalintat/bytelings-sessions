"""Rung 4: Solo — solved version.

`tomllib.load` accepts a binary file handle (opened with `"rb"`).
We write the result as JSON with `indent=2, sort_keys=True` so the
output is deterministic and diff-friendly.
"""
import json
import tomllib
from pathlib import Path


def toml_to_json(toml_path: Path, json_path: Path) -> dict:
    with open(toml_path, "rb") as f:
        data = tomllib.load(f)
    json_path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    return data
