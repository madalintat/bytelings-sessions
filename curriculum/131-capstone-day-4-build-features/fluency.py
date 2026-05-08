"""Rung 2: Fluency drill — fix the config loader.

Topic: tomllib.loads (stdlib, Python 3.11+)

`load_config` reads a TOML string and returns a dict for the named tool.
Currently it uses json.loads on TOML content — that crashes. Fix it.

Two TODOs below. The only change needed is how you parse `content`.
"""
from __future__ import annotations

import json  # noqa: F401 — remove this once you switch to tomllib

DEFAULTS: dict = {
    "rules": None,
    "function-too-long-max": 50,
    "nested-loop-depth-max": 3,
    "exclude": [],
}


def load_config(content: str, tool_name: str) -> dict:
    """Parse TOML `content` and return merged config for `tool_name`.

    If the TOML has no [tool.<tool_name>] section, returns a copy of DEFAULTS.
    Otherwise merges DEFAULTS with the tool-specific overrides.

    Args:
        content:   Raw TOML text (e.g. from pyproject.toml).
        tool_name: The tool name key under [tool], e.g. "my-lint".
    """
    # TODO 1: replace json.loads with the correct tomllib call.
    #         json.loads cannot parse TOML — they are different formats.
    data = json.loads(content)  # BUG: should use tomllib.loads(content)

    # TODO 2: extract the right section from `data`.
    #         The section is data["tool"][tool_name], not data[tool_name].
    user = data.get(tool_name, {})  # BUG: should be data.get("tool", {}).get(tool_name, {})
    return {**DEFAULTS, **user}
