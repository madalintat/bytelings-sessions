"""Rung 2: Fluency drill — solved version.

The two bugs were:
  1. tomllib.loads takes a *str*, not bytes. Calling .encode() raised
     TypeError. Remove the .encode() call.
  2. The loop appended an error for *every* field unconditionally.
     The fix: only append when the field is absent from parsed data.
"""
from __future__ import annotations
import tomllib

SAMPLE_PYPROJECT = """
[project]
name = "my-linter"
version = "0.1.0"
requires-python = ">=3.12"

[project.scripts]
my-linter = "my_linter.main"
"""

REQUIRED_FIELDS = ["project", "build-system"]


def validate_pyproject(toml_str: str) -> list[str]:
    """Parse toml_str and return one error string per missing required field."""
    data = tomllib.loads(toml_str)  # fix 1: no .encode()
    errors: list[str] = []
    for name in REQUIRED_FIELDS:
        if name not in data:          # fix 2: only flag absent fields
            errors.append(f"missing required table: {name}")
    return errors
