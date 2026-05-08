"""Solved: solo — mutable_default_argument rule via @rule_for.

Key insight: node.args.defaults are the DEFAULT VALUES (the right-hand
side of `=`). node.args.args are the PARAMETER NAMES. Iterating the
wrong one gives type errors or misses the check entirely.

ast.AsyncFunctionDef is a separate node type — registering for both
handles async functions. Alternatively, check isinstance for both types
inside a single rule.
"""
from __future__ import annotations
import ast
from dataclasses import dataclass


@dataclass
class Finding:
    line: int
    rule: str
    message: str


_REGISTRY: dict[type, list] = {}


def rule_for(node_type: type):
    """Decorator: register a rule function for *node_type*."""
    def decorator(fn):
        _REGISTRY.setdefault(node_type, []).append(fn)
        return fn
    return decorator


def _check_mutable(node, _ctx):
    """Shared logic for FunctionDef and AsyncFunctionDef."""
    for default in node.args.defaults:
        if isinstance(default, (ast.List, ast.Dict, ast.Set)):
            return Finding(
                default.lineno,
                "E002",
                f"mutable default argument in {node.name}",
            )
    return None


@rule_for(ast.FunctionDef)
def mutable_default_argument(node: ast.FunctionDef, ctx: dict) -> Finding | None:
    """E002 — mutable default argument (list, dict, or set literal)."""
    return _check_mutable(node, ctx)


@rule_for(ast.AsyncFunctionDef)
def mutable_default_argument_async(node: ast.AsyncFunctionDef, ctx: dict) -> Finding | None:
    """E002 — same rule applied to async functions."""
    return _check_mutable(node, ctx)


class Linter(ast.NodeVisitor):
    def __init__(self):
        self.findings: list[Finding] = []

    def visit(self, node: ast.AST):
        for rule_fn in _REGISTRY.get(type(node), []):
            result = rule_fn(node, {})
            if result is not None:
                self.findings.append(result)
        self.generic_visit(node)

    def run(self, source: str) -> list[Finding]:
        tree = ast.parse(source)
        self.visit(tree)
        return sorted(self.findings, key=lambda f: f.line)
