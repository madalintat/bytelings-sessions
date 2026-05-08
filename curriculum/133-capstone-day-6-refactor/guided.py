"""Rung 3: Guided implement — console-script target lookup.

Topic: navigating nested TOML dicts

`console_script_target(toml_str, command_name)` looks up the
entry-point string for a named console-script in a pyproject.toml.

The shape in pyproject.toml:

    [project.scripts]
    my-tool = "my_pkg.cli:main"

So `console_script_target(toml, "my-tool")` → `"my_pkg.cli:main"`.
Returns None if [project.scripts] is absent or the command is not listed.

Fill in the function body. Use only tomllib (stdlib).
"""
from __future__ import annotations
import tomllib


def console_script_target(toml_str: str, command_name: str) -> str | None:
    """Return the entry-point string for command_name, or None if absent.

    Examples:
        >>> toml = '[project.scripts]\\nmy-tool = "my_pkg.cli:main"\\n'
        >>> console_script_target(toml, "my-tool")
        'my_pkg.cli:main'
        >>> console_script_target(toml, "missing")
        None
    """
    # TODO: parse toml_str, navigate project -> scripts, return the value
    # for command_name, or None if any key in the chain is missing.
    raise NotImplementedError
