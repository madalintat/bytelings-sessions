"""Rung 2: Fluency drill — solved version.

The bug: the function always returned False.
Fix: check whether the literal string 'id-token: write' is a substring
of yaml_str. The `in` operator handles it in one line.
"""
from __future__ import annotations

SAMPLE_WORKFLOW = """\
name: Release

on:
  push:
    tags: ["v*"]

jobs:
  pypi-publish:
    name: Publish to PyPI
    runs-on: ubuntu-latest
    environment:
      name: pypi
      url: https://pypi.org/project/my-linter/
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install build && python -m build
      - uses: pypa/gh-action-pypi-publish@release/v1
"""


def has_id_token_write(yaml_str: str) -> bool:
    """Return True if 'id-token: write' is present in yaml_str."""
    return "id-token: write" in yaml_str
