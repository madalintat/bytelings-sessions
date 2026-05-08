"""Rung 3: Guided implement — solved version.

Total parameter count = len(args) + len(posonlyargs) + len(kwonlyargs).
*args and **kwargs are deliberately excluded (vararg / kwarg slots).

An issue is raised when total > limit (strictly greater than, not >=).
"""
from __future__ import annotations

import ast
from dataclasses import dataclass


@dataclass
class Issue:
    line: int
    code: str
    message: str


def check_too_many_params(source: str, limit: int = 6) -> list[Issue]:
    """Return Issue per function with > `limit` named parameters (M002).

    Message format: '<name> has <n> parameters (limit: <limit>)'

    >>> issues = check_too_many_params("def f(a,b,c,d,e,f,g): pass", limit=6)
    >>> len(issues), issues[0].code
    (1, 'M002')
    """
    issues: list[Issue] = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            total = (
                len(node.args.args)
                + len(node.args.posonlyargs)
                + len(node.args.kwonlyargs)
            )
            if total > limit:
                issues.append(
                    Issue(
                        node.lineno,
                        "M002",
                        f"{node.name} has {total} parameters (limit: {limit})",
                    )
                )
    return issues
