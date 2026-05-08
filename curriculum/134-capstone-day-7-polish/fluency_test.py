"""Tests for rung 2 — green after the TODO is fixed."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


GOOD_WORKFLOW = """\
name: Release
on:
  push:
    tags: ["v*"]
jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    environment:
      name: pypi
      url: https://pypi.org/project/my-linter/
    steps:
      - uses: actions/checkout@v4
      - uses: pypa/gh-action-pypi-publish@release/v1
"""

NO_PERM_WORKFLOW = ex.SAMPLE_WORKFLOW


def test_present_returns_true():
    result = ex.has_id_token_write(GOOD_WORKFLOW)
    diagnose(
        result is True,
        "Expected True when 'id-token: write' is in the workflow string.",
        (lambda: result is False,
         "Returned False — check you're searching for the literal "
         "substring 'id-token: write', not something else."),
    )


def test_absent_returns_false():
    result = ex.has_id_token_write(NO_PERM_WORKFLOW)
    diagnose(
        result is False,
        "Expected False when 'id-token: write' is NOT in the workflow string.",
        (lambda: result is True,
         "Returned True for the broken sample — that workflow lacks the permission."),
    )


def test_empty_string():
    result = ex.has_id_token_write("")
    diagnose(
        result is False,
        "Expected False for an empty string.",
    )


def test_partial_match_not_enough():
    result = ex.has_id_token_write("id-token: read\n")
    diagnose(
        result is False,
        "Expected False — 'id-token: read' is not 'id-token: write'.",
        (lambda: result is True,
         "Matched 'id-token: read' as if it were 'id-token: write'. "
         "Search for the full literal string."),
    )
