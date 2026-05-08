"""Solved: guided — rule_for decorator + Linter.visit dispatch.

rule_for: uses dict.setdefault to create-or-append, then returns fn.
Linter.visit: looks up type(node), calls each handler, then recurses.
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
        # setdefault ensures the list exists; append stores the function.
        _REGISTRY.setdefault(node_type, []).append(fn)
        return fn
    return decorator


@rule_for(ast.ExceptHandler)
def bare_except(node: ast.ExceptHandler, ctx: dict) -> Finding | None:
    """E001 — bare `except:` catches all exceptions."""
    if node.type is None:
        return Finding(node.lineno, "E001", "bare except: catches all exceptions")
    return None


class Linter(ast.NodeVisitor):
    """Walk an AST and collect findings from all registered rules."""

    def __init__(self):
        self.findings: list[Finding] = []

    def visit(self, node: ast.AST):
        # Dispatch to every rule whose key matches this node's type.
        for rule_fn in _REGISTRY.get(type(node), []):
            result = rule_fn(node, {})
            if result is not None:
                self.findings.append(result)
        # Recurse into child nodes (required — NodeVisitor.visit doesn't do this).
        self.generic_visit(node)

    def run(self, source: str) -> list[Finding]:
        tree = ast.parse(source)
        self.visit(tree)
        return sorted(self.findings, key=lambda f: f.line)
