"""Solved: fluency — fixed unused-import scanner with Attribute-chain walking.

The fix: after collecting bare ast.Name nodes, also walk every
ast.Attribute chain down to its root Name and collect that name.

In `os.path.join(...)` the AST is:
    Attribute(value=Attribute(value=Name(id='os'), attr='path'), attr='join')
Descending .value until we hit a Name gives us 'os'.
"""
from __future__ import annotations
import ast


def find_unused_imports(source: str) -> set[str]:
    """Return the set of imported names that are never used in *source*."""
    tree = ast.parse(source)

    # Pass 1: collect imported names.
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.asname if alias.asname else alias.name
                imported.add(name)

    # Pass 2: collect used names (bare Names + roots of Attribute chains).
    used: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
        elif isinstance(node, ast.Attribute):
            # Walk down the .value chain to find the root Name.
            root = node.value
            while isinstance(root, ast.Attribute):
                root = root.value
            if isinstance(root, ast.Name):
                used.add(root.id)

    return imported - used
