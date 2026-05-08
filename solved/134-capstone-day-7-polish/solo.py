"""Rung 4: Solo — solved version.

Each check is a simple substring test. The complaints list accumulates
one entry per failing check and is returned at the end.
"""
from __future__ import annotations


def validate_publish_workflow(yaml_str: str) -> list[str]:
    """Return a list of complaint strings for workflow problems, or []."""
    complaints: list[str] = []

    if "id-token: write" not in yaml_str:
        complaints.append(
            "missing 'id-token: write' permission — required for Trusted Publishing"
        )

    if "environment:" not in yaml_str:
        complaints.append(
            "missing 'environment:' block — required for Trusted Publishing"
        )
    elif "name: pypi" not in yaml_str:
        complaints.append(
            "environment block is missing 'name: pypi'"
        )

    if "--repository-url" in yaml_str:
        complaints.append(
            "found '--repository-url' — use Trusted Publishing instead of legacy URL"
        )

    if "password:" in yaml_str:
        complaints.append(
            "found 'password:' — remove hardcoded credentials; use Trusted Publishing"
        )

    return complaints
