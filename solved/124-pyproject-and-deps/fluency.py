"""Rung 2: Fluency drill — solved version.

Two bugs fixed:
1. `tomllib.loads` takes a `str`, not `bytes`.  The starter called
   `.encode()` on the input, converting str → bytes, which raises
   TypeError.  Drop the `.encode()`.
2. `list_dependencies` raised KeyError when 'dependencies' was absent.
   Use `.get()` with a default of `[]` instead.
"""
import tomllib


def parse_project_name(toml_text: str) -> str:
    """Return the value of [project].name from a TOML string."""
    data = tomllib.loads(toml_text)
    return data["project"]["name"]


def list_dependencies(toml_text: str) -> list[str]:
    """Return the [project].dependencies list, or [] if missing."""
    data = tomllib.loads(toml_text)
    return data["project"].get("dependencies", [])
