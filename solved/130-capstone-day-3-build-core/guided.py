"""Solved: guided — find_unused_imports returning sorted list.

Two-pass approach:
  Pass 1: collect {name: lineno} from ast.Import nodes.
  Pass 2: collect all used names (Name nodes + Attribute root names).
  Result: sorted(imported_names - used_names).
"""
from __future__ import annotations
import ast


def find_unused_imports(source: str) -> list[str]:
    """Return sorted list of unused import names in *source*."""
    tree = ast.parse(source)

    # Pass 1: name -> lineno mapping.
    imported: dict[str, int] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.asname if alias.asname else alias.name
                imported[name] = node.lineno

    # Pass 2: collect every name that is referenced.
    used: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
        elif isinstance(node, ast.Attribute):
            root = node.value
            while isinstance(root, ast.Attribute):
                root = root.value
            if isinstance(root, ast.Name):
                used.add(root.id)

    return sorted(imported.keys() - used)
