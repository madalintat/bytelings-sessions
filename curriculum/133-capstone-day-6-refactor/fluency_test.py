"""Tests for rung 2 — green after both TODOs are fixed."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


COMPLETE = """
[project]
name = "my-linter"
version = "0.1.0"

[project.scripts]
my-linter = "my_linter.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
"""

MISSING_BUILD = """
[project]
name = "my-linter"
version = "0.1.0"
"""

MISSING_PROJECT = """
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
"""


def test_complete_returns_empty():
    result = ex.validate_pyproject(COMPLETE)
    diagnose(
        result == [],
        f"Expected [] for a complete pyproject, got {result!r}",
        (lambda: isinstance(result, list) and len(result) > 0,
         "validate_pyproject returned errors for a valid pyproject — "
         "make sure you only flag fields that are actually missing."),
    )


def test_missing_build_system():
    result = ex.validate_pyproject(MISSING_BUILD)
    diagnose(
        "missing required table: build-system" in result,
        "Expected an error about 'build-system' when that table is absent.",
        (lambda: result == [],
         "validate_pyproject returned [] — it isn't checking for missing fields yet."),
        (lambda: any("project" in e for e in result),
         "validate_pyproject reported 'project' as missing but 'project' IS present."),
    )


def test_missing_project():
    result = ex.validate_pyproject(MISSING_PROJECT)
    diagnose(
        "missing required table: project" in result,
        "Expected an error about 'project' when that table is absent.",
        (lambda: result == [],
         "validate_pyproject returned [] — it isn't checking for missing fields yet."),
    )


def test_missing_both():
    result = ex.validate_pyproject("")
    diagnose(
        len(result) == 2,
        f"Expected 2 errors for an empty TOML string, got {len(result)}: {result!r}",
        (lambda: result == [],
         "validate_pyproject returned [] for an empty string — "
         "both 'project' and 'build-system' should be flagged."),
    )
