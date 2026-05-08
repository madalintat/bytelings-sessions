"""Rung 4: Solo implement — full workflow validator.

Topic: combining multiple string-search checks into a list of complaints

Implement `validate_publish_workflow(yaml_str) -> list[str]`.

Return a complaint string for EACH of the following problems found:
  1. Missing `id-token: write` permission.
  2. Missing `environment:` block (look for the literal line that
     starts with spaces and contains 'environment:').
  3. Missing `name: pypi` under the environment block.
  4. Presence of `--repository-url` (regression: should use Trusted
     Publishing, not legacy URL flag).
  5. Presence of `password:` (regression: no hardcoded credentials).

Return [] if none of the above are found (clean workflow).
Hidden tests check each complaint independently and the clean case.
"""
from __future__ import annotations


def validate_publish_workflow(yaml_str: str) -> list[str]:
    """Return a list of complaint strings for workflow problems.

    Returns [] for a clean workflow.
    """
    raise NotImplementedError
