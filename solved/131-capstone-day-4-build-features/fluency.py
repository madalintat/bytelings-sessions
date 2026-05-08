"""Rung 2: Fluency drill — solved version.

Key fix: switch from the JSON parser to tomllib (the stdlib TOML
parser shipped in Python 3.11+). The tool section lives at
data["tool"][tool_name], not data[tool_name].
"""
from __future__ import annotations

import tomllib

DEFAULTS: dict = {
    "rules": None,
    "function-too-long-max": 50,
    "nested-loop-depth-max": 3,
    "exclude": [],
}


def load_config(content: str, tool_name: str) -> dict:
    """Parse TOML `content` and return merged config for `tool_name`."""
    # tomllib.loads expects a str; tomllib.load expects a binary file handle.
    data = tomllib.loads(content)
    # pyproject.toml nests tool config under [tool.<name>].
    user = data.get("tool", {}).get(tool_name, {})
    return {**DEFAULTS, **user}
