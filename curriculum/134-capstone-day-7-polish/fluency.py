"""Rung 2: Fluency drill — check a GitHub Actions release workflow.

Topic: string search on structured text

The SAMPLE_WORKFLOW string below is BROKEN: the pypi-publish job
is missing the `id-token: write` permission needed for Trusted
Publishing (OIDC). Without it, the publish step fails with a 403.

Learner task: implement `has_id_token_write(yaml_str)` that returns
True if the string `id-token: write` appears anywhere in the yaml_str,
False otherwise. No YAML parser required — a substring search is fine
because the test inputs are well-structured and controlled.

One TODO below.
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
    """Return True if 'id-token: write' is present in yaml_str.

    Examples:
        >>> has_id_token_write("permissions:\\n  id-token: write\\n")
        True
        >>> has_id_token_write("permissions:\\n  contents: read\\n")
        False
    """
    # TODO: return True when the literal string "id-token: write" appears
    # anywhere in yaml_str, False otherwise.
    return False   # BUG: always returns False
