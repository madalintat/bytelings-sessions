"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: round-trip a TOML config to a JSON cache

Implement `toml_to_json(toml_path, json_path)`:
- Read `toml_path` with tomllib.
- Write the result to `json_path` as JSON, indented 2, sort_keys=True.
- Return the loaded dict.

Constraints:
- Use tomllib (read-only). It's standard library on Python 3.11+.
- tomllib.loads operates on a string but you can also use
  tomllib.load(fp) on a binary file handle. Either works.
- Use pathlib for path handling.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import json
import tomllib
from pathlib import Path


def toml_to_json(toml_path: Path, json_path: Path) -> dict:
    raise NotImplementedError
