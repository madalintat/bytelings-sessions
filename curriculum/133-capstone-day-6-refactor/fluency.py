"""Rung 2: Fluency drill — validate a pyproject.toml string.

Topic: tomllib + required-field validation

The SAMPLE_PYPROJECT string below is broken in two ways:
  1. It is missing the [build-system] table entirely.
  2. The [project.scripts] entry uses a bare dotted name instead
     of the required 'module:attr' form.

Learner task: implement `validate_pyproject(toml_str)` that parses
the TOML and returns a list of human-readable error strings for each
of the REQUIRED_FIELDS that is missing from the top-level table.

Required top-level fields are: 'project' and 'build-system'.

Two TODOs below.
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
    """Parse toml_str and return one error string per missing required field.

    Returns [] if all required fields are present.

    Example:
        >>> validate_pyproject('[project]\\nname="x"\\n')
        ['missing required table: build-system']
    """
    # TODO: parse toml_str with tomllib.loads (takes str, not bytes)
    data = tomllib.loads(toml_str.encode())  # BUG: .encode() makes it bytes
    errors: list[str] = []
    # TODO: for each name in REQUIRED_FIELDS, check presence in data.
    # Append f"missing required table: {name}" if absent.
    for name in REQUIRED_FIELDS:
        errors.append(f"missing required table: {name}")
    return errors
