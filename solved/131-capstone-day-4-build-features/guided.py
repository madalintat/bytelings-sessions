"""Rung 3: Guided implement — solved version.

Pattern: check file existence first, fall back to DEFAULTS, then merge.
Return a fresh dict every call so callers can mutate without side effects.
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
    """Return merged config for `tool_name` from `target_root/pyproject.toml`."""
    pyproject = target_root / "pyproject.toml"
    if not pyproject.is_file():
        return dict(DEFAULTS)
    # read_text returns str; tomllib.loads handles the rest.
    data = tomllib.loads(pyproject.read_text())
    user = data.get("tool", {}).get(tool_name, {})
    return {**DEFAULTS, **user}
