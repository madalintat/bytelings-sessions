"""Rung 2: Fluency drill — solved version.

Two bugs fixed:
1. `count_functions` used `isinstance(n, ast.FunctionDef)` which also
   matches AsyncFunctionDef via inheritance in some Python versions.
   Using `type(n) is ast.FunctionDef` is exact and excludes async.
2. `names_assigned` appended the Name *node* itself instead of `target.id`
   (the string attribute holding the variable name).
"""
from __future__ import annotations

import ast


def count_functions(source: str) -> int:
    """Return the number of function definitions in source.

    Counts both top-level and nested functions.  Does NOT count async functions.
    """
    tree = ast.parse(source)
    return sum(1 for n in ast.walk(tree) if type(n) is ast.FunctionDef)


def names_assigned(source: str) -> list[str]:
    """Return all simple-target names that get assigned to, in order of appearance."""
    tree = ast.parse(source)
    out: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    out.append(target.id)
    return out
