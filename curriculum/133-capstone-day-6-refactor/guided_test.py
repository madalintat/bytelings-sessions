"""Tests for rung 3."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE = """
[project]
name = "my-linter"
version = "0.1.0"

[project.scripts]
my-linter = "my_linter.cli:main"
lint = "my_linter.cli:lint_cmd"
"""

NO_SCRIPTS = """
[project]
name = "my-linter"
version = "0.1.0"
"""


def test_finds_command():
    result = ex.console_script_target(SAMPLE, "my-linter")
    diagnose(
        result == "my_linter.cli:main",
        f"Expected 'my_linter.cli:main', got {result!r}",
        (lambda: result is None,
         "Returned None — did you navigate data['project']['scripts']?"),
    )


def test_finds_second_command():
    result = ex.console_script_target(SAMPLE, "lint")
    diagnose(
        result == "my_linter.cli:lint_cmd",
        f"Expected 'my_linter.cli:lint_cmd', got {result!r}",
    )


def test_missing_command_returns_none():
    result = ex.console_script_target(SAMPLE, "not-there")
    diagnose(
        result is None,
        f"Expected None for an absent command, got {result!r}",
        (lambda: isinstance(result, str),
         "Returned a string instead of None — use .get() to avoid KeyError."),
    )


def test_no_scripts_table_returns_none():
    result = ex.console_script_target(NO_SCRIPTS, "my-linter")
    diagnose(
        result is None,
        f"Expected None when [project.scripts] is absent, got {result!r}",
        (lambda: isinstance(result, str),
         "Raised or returned a value — guard against missing 'scripts' key."),
    )
