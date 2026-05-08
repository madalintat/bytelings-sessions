"""Rung 4: Solo implement — solved version.

check_print_statements: find bare `print(...)` calls at module top level.
'Top level' means the call is a direct child of the module body — not
inside a FunctionDef, AsyncFunctionDef, or ClassDef.  We check this by
only walking the module's immediate statements (not recursing into
function/class bodies).

lint: merges M001, M002, M003, sorted by line number (stable).
"""
from __future__ import annotations

import ast
import sys
from dataclasses import dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent
_f = spec_from_file_location("_d127_fluency", _HERE / "fluency.py")
_fluency = module_from_spec(_f)
sys.modules["_d127_fluency"] = _fluency
_f.loader.exec_module(_fluency)
_g = spec_from_file_location("_d127_guided", _HERE / "guided.py")
_guided = module_from_spec(_g)
sys.modules["_d127_guided"] = _guided
_g.loader.exec_module(_guided)


@dataclass
class Issue:
    line: int
    code: str
    message: str


def _is_bare_print_call(node: ast.AST) -> bool:
    """Return True if node is a Call to the bare name 'print'."""
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "print"
    )


def check_print_statements(source: str) -> list[Issue]:
    """Return Issue for each top-level print() call (M003).

    Top-level means directly inside the module body, not inside a
    function or class definition.
    """
    tree = ast.parse(source)
    issues: list[Issue] = []
    # Only examine top-level statements in the module body.
    for stmt in tree.body:
        # Skip function/class definitions — print inside them is fine.
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        # An Expr wrapping a Call is the shape of a bare function call statement.
        if isinstance(stmt, ast.Expr) and _is_bare_print_call(stmt.value):
            issues.append(
                Issue(
                    stmt.lineno,
                    "M003",
                    "print() call at top-level — use logging instead",
                )
            )
    return issues


def lint(source: str, *, max_params: int = 6) -> list[Issue]:
    """Run all three rules and return issues sorted by line number."""
    raw: list[Issue] = []
    for issue in _fluency.check_mutable_defaults(source):
        raw.append(Issue(issue.line, issue.code, issue.message))
    for issue in _guided.check_too_many_params(source, limit=max_params):
        raw.append(Issue(issue.line, issue.code, issue.message))
    raw.extend(check_print_statements(source))
    raw.sort(key=lambda i: i.line)
    return raw
