"""Rung 3: Guided implement — solved version.

Algorithm:
- Walk the AST in source order (collected with lineno, then sorted).
- ast.Import: emit each alias.name directly (aliases ignored per spec).
- ast.ImportFrom: build a prefix from `level` dots + module name.
  Join prefix and alias.name with '.' only when both are non-empty.
  Edge cases:
    `from . import x`    → level=1, module=None → prefix=".", entry=".x"
    `from .. import x`   → level=2, module=None → prefix="..", entry="..x"
    `from .helpers import a` → level=1, module="helpers" → ".helpers.a"

>>> list_imports("import os\\nfrom pathlib import Path")
['os', 'pathlib.Path']
>>> list_imports("from . import a")
['.a']
"""
from __future__ import annotations

import ast


def _import_from_entry(node: ast.ImportFrom, alias: ast.alias) -> str:
    """Normalise a single name from an ImportFrom node to a dotted string."""
    dots = "." * (node.level or 0)
    module = node.module or ""
    # Join dots and module only when module is non-empty.
    prefix = dots + module if module else dots
    # Join prefix and alias only when prefix is non-empty.
    if prefix:
        return f"{prefix}.{alias.name}" if not prefix.endswith(".") else f"{prefix}{alias.name}"
    return alias.name


def list_imports(source: str) -> list[str]:
    """Return imports in source order, normalised to dotted strings."""
    tree = ast.parse(source)
    items: list[tuple[int, int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                items.append((node.lineno, node.col_offset, alias.name))
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                items.append((node.lineno, node.col_offset,
                               _import_from_entry(node, alias)))
    items.sort(key=lambda t: (t[0], t[1]))
    return [s for _, _, s in items]
