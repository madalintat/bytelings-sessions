"""Rung 3: Guided implement — load config from pyproject.toml on disk.

Topic: tomllib + pathlib + merging dicts

Implement `load_config(target_root, tool_name)`:
- Look for `pyproject.toml` in `target_root`.
- If the file is missing, return a copy of DEFAULTS.
- Otherwise parse it with tomllib, merge DEFAULTS with
  data["tool"][tool_name] (if that section exists), and return the result.

The pattern:
    pyproject = target_root / "pyproject.toml"
    if not pyproject.is_file():
        return dict(DEFAULTS)
    data = tomllib.loads(pyproject.read_text())   # or tomllib.load(fp) in 'rb' mode
    user = data.get("tool", {}).get(tool_name, {})
    return {**DEFAULTS, **user}
"""
from __future__ import annotations

import tomllib
from pathlib import Path

DEFAULTS: dict = {
    "rules": None,
    "function-too-long-max": 50,
    "nested-loop-depth-max": 3,
    "exclude": [],
}


def load_config(target_root: Path, tool_name: str) -> dict:
    """Return merged config for `tool_name` from `target_root/pyproject.toml`.

    Falls back to DEFAULTS when the file or section is absent.
    """
    # TODO: implement per the module docstring above.
    raise NotImplementedError
