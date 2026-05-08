"""Rung 2: Fluency drill — solved version.

Two bugs fixed:
1. `parse_entry_point` split on '.' instead of ':'.  The separator
   between module path and attribute in an entry-point spec is always ':'.
2. `is_valid_entry_point` accepted ':main' and 'habit_cli:' because it
   only checked that exactly one ':' existed.  The fix also requires
   both sides to be non-empty after stripping.
"""
from __future__ import annotations


def parse_entry_point(spec: str) -> tuple[str, str]:
    """Parse 'module.path:attr' into (module, attr)."""
    module, attr = spec.split(":", 1)
    return module, attr


def is_valid_entry_point(spec: str) -> bool:
    """Return True if spec has exactly one ':' with non-empty sides."""
    if spec.count(":") != 1:
        return False
    module, attr = spec.split(":", 1)
    return bool(module.strip()) and bool(attr.strip())
