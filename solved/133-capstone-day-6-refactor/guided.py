"""Rung 3: Guided — solved version.

Navigate the nested dict with .get() at each level so missing keys
return None cleanly instead of raising KeyError.
"""
from __future__ import annotations
import tomllib


def console_script_target(toml_str: str, command_name: str) -> str | None:
    """Return the entry-point string for command_name, or None if absent."""
    data = tomllib.loads(toml_str)
    scripts = data.get("project", {}).get("scripts", {})
    return scripts.get(command_name)
