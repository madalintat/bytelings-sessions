"""Rung 4: Solo implement — parse project.dependencies.

Topic: simple PEP 508 subset parsing (no full grammar)

Implement `parse_dependencies(toml_str)` returning a list of
(package_name, version_spec) tuples from [project].dependencies.

Handle:
  - bare name:            "pytest"           → ("pytest", "")
  - single specifier:     "pytest>=8.0"      → ("pytest", ">=8.0")
  - compound specifier:   "pytest>=8.0,<9"   → ("pytest", ">=8.0,<9")
  - leading/trailing whitespace in each entry

Use a simple scan for the first specifier character (any of: < > = ! ~).
Return [] when [project].dependencies is missing.
Hidden tests cover all three cases plus missing-key.
"""
from __future__ import annotations


def parse_dependencies(toml_str: str) -> list[tuple[str, str]]:
    """Return [(package_name, version_spec), ...] from project.dependencies.

    Examples:
        >>> parse_dependencies('[project]\\ndependencies = ["pytest>=8.0","rich"]\\n')
        [('pytest', '>=8.0'), ('rich', '')]
    """
    raise NotImplementedError
