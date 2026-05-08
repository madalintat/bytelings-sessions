"""Rung 2: Fluency drill — fix two AST walks.

Topic: ast.parse + ast.walk + isinstance checks
"""
from __future__ import annotations
import ast


def count_functions(source: str) -> int:
    """Return the number of function definitions in `source`.

    Counts both top-level and nested functions. Does NOT count async functions.
    (We'll add async on day 127.)
    """
    tree = ast.parse(source)
    # TODO: this also matches AsyncFunctionDef because of inheritance.
    # Use type(n) is FunctionDef instead — or just exclude AsyncFunctionDef explicitly.
    return sum(1 for n in ast.walk(tree) if isinstance(n, ast.FunctionDef))


def names_assigned(source: str) -> list[str]:
    """Return all simple-target names that get assigned to, in order of appearance.

    For `x = 1`, the target is a Name node with id='x'. We ignore tuple
    targets and attribute targets for now.
    """
    tree = ast.parse(source)
    out: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                # TODO: this appends the Name node itself, not its id.
                if isinstance(target, ast.Name):
                    out.append(target)
    return out
