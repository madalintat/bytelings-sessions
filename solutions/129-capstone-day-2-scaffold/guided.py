"""Rung 3: Guided implement — registry + NodeVisitor dispatch.

Topic: @rule_for(node_type) wired into ast.NodeVisitor.visit

Fill in the two TODOs below:

1. `rule_for(node_type)` — a decorator that stores a function in
   _REGISTRY[node_type] (a list, so multiple rules per type work).

2. `Linter.visit(self, node)` — look up the node's type in _REGISTRY,
   call each matching function with (node, ctx), then recurse with
   generic_visit so the whole tree is walked.

The `bare_except` rule is already implemented as an example.
"""
from __future__ import annotations
import ast
from dataclasses import dataclass, field


@dataclass
class Finding:
    line: int
    rule: str
    message: str


# Maps ast node TYPE -> list of rule functions (node, ctx) -> Finding | None
_REGISTRY: dict[type, list] = {}


def rule_for(node_type: type):
    """Decorator: register a rule function for *node_type*.

    Usage::

        @rule_for(ast.FunctionDef)
        def my_rule(node, ctx):
            ...

    TODO: implement this decorator so it appends *fn* to
    _REGISTRY[node_type] (create the list if absent) and returns *fn*
    unchanged.
    """
    def decorator(fn):
        raise NotImplementedError  # TODO: append fn to _REGISTRY[node_type]
    return decorator


# ── already-implemented rule — do not modify ──────────────────────────────────

@rule_for(ast.ExceptHandler)
def bare_except(node: ast.ExceptHandler, ctx: dict) -> Finding | None:
    """E001 — bare `except:` catches everything including KeyboardInterrupt."""
    if node.type is None:
        return Finding(node.lineno, "E001", "bare except: catches all exceptions")
    return None


# ── Linter ────────────────────────────────────────────────────────────────────

class Linter(ast.NodeVisitor):
    """Walk an AST and collect findings from all registered rules."""

    def __init__(self):
        self.findings: list[Finding] = []

    def visit(self, node: ast.AST):
        """Dispatch *node* to every rule registered for its type.

        TODO: look up type(node) in _REGISTRY, call each rule function
        with (node, {}) and append non-None results to self.findings,
        then call self.generic_visit(node) to recurse into children.
        """
        raise NotImplementedError

    def run(self, source: str) -> list[Finding]:
        tree = ast.parse(source)
        self.visit(tree)
        return sorted(self.findings, key=lambda f: f.line)
