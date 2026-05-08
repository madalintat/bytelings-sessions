"""Rung 2: Fluency drill — fix the entry-point string parser.

Topic: 'module:attr' notation

A console script entry-point string looks like 'habit_cli.cli:main'.
Two TODOs below.
"""
from __future__ import annotations


def parse_entry_point(spec: str) -> tuple[str, str]:
    """Parse 'module.path:attr' into (module, attr)."""
    # TODO: split on the wrong separator
    module, attr = spec.split(".", 1)
    return module, attr


def is_valid_entry_point(spec: str) -> bool:
    """Return True if spec has exactly one ':' with non-empty sides."""
    # TODO: this accepts 'foo:' and ':bar' as valid. Tighten it.
    return spec.count(":") == 1
