"""Rung 4: Solo — solved version.

Strategy: scan each requirement string for the first specifier
character (one of < > = ! ~), split there. Everything before is the
package name; everything from that character onward is the version spec.
Strip whitespace throughout.
"""
from __future__ import annotations
import tomllib

_SPEC_CHARS = frozenset("<>=!~")


def _split_req(req: str) -> tuple[str, str]:
    req = req.strip()
    for i, ch in enumerate(req):
        if ch in _SPEC_CHARS:
            return req[:i].strip(), req[i:].strip()
    return req, ""


def parse_dependencies(toml_str: str) -> list[tuple[str, str]]:
    """Return [(package_name, version_spec), ...] from project.dependencies."""
    data = tomllib.loads(toml_str)
    raw = data.get("project", {}).get("dependencies", [])
    return [_split_req(r) for r in raw]
