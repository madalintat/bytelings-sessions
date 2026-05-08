"""Rung 2: Fluency drill — fix the M001 (mutable defaults) check.

Topic: ast.FunctionDef.args.defaults
"""
from __future__ import annotations
import ast
from dataclasses import dataclass


@dataclass
class Issue:
    line: int
    code: str
    message: str


def check_mutable_defaults(source: str) -> list[Issue]:
    """Return one Issue per mutable default argument.

    Triggers on list/dict/set literals as default values.
    """
    issues: list[Issue] = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        # TODO: this also fires on AsyncFunctionDef via FunctionDef inheritance — fine.
        # But it iterates over node.args.args (parameter NAMES) instead of node.args.defaults.
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for default in node.args.args:
                # TODO: Tuple is also a literal but it's IMMUTABLE — don't flag it.
                if isinstance(default, (ast.List, ast.Dict, ast.Set, ast.Tuple)):
                    issues.append(
                        Issue(default.lineno, "M001",
                              f"mutable default in {node.name}"))
    return issues
