"""Rung 4: Solo implement — solved version.

summarize_project merges two possible sources for dev deps:
  - [project.optional-dependencies] dev key
  - [tool.uv] dev-dependencies key

Both are normalised through split_requirement (strip specifiers),
then merged into a deduped sorted list.

Missing keys are handled with chained .get() calls returning [] or "".
"""
from __future__ import annotations

import tomllib

_SPEC_CHARS = frozenset("=<>!~")


def _name_only(req: str) -> str:
    """Return just the package name from a PEP 508 requirement string."""
    req = req.strip()
    for i, ch in enumerate(req):
        if ch in _SPEC_CHARS:
            return req[:i].strip()
    return req


def summarize_project(toml_text: str) -> dict:
    """Parse pyproject.toml text and return a project summary dict."""
    data = tomllib.loads(toml_text)
    project = data.get("project", {})

    name: str = project.get("name", "")
    version: str = project.get("version", "")
    python: str = project.get("requires-python", "")

    deps: list[str] = [_name_only(r) for r in project.get("dependencies", [])]

    opt_dev: list[str] = [
        _name_only(r)
        for r in project.get("optional-dependencies", {}).get("dev", [])
    ]
    uv_dev: list[str] = [
        _name_only(r)
        for r in data.get("tool", {}).get("uv", {}).get("dev-dependencies", [])
    ]
    dev_deps: list[str] = sorted(set(opt_dev) | set(uv_dev))

    return {
        "name": name,
        "version": version,
        "python": python,
        "deps": deps,
        "dev_deps": dev_deps,
    }
