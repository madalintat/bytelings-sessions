"""Rung 2: Fluency drill — solved version.

Two bugs fixed:
1. The loop iterated over `node.args.args` (the list of *parameter name*
   nodes) instead of `node.args.defaults` (the list of *default value*
   nodes).  Only defaults can be mutable.
2. The code flagged `ast.Tuple` as mutable.  Tuples are immutable; they
   are fine as default values and must not be reported.
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
    """Return one Issue per mutable default argument (M001).

    Triggers on list/dict/set literals as default values.
    Tuples are immutable and are NOT flagged.
    """
    issues: list[Issue] = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for default in node.args.defaults:
                if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                    issues.append(
                        Issue(
                            default.lineno,
                            "M001",
                            f"mutable default in {node.name}",
                        )
                    )
    return issues
