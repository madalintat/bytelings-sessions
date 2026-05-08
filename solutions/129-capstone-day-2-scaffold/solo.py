"""Rung 4: Solo implement — mutable_default_argument rule.

Topic: @rule_for(ast.FunctionDef) with default-value inspection

Implement `mutable_default_argument` as a rule registered via
@rule_for(ast.FunctionDef).

Rule logic:
- Walk node.args.defaults (NOT node.args.args — those are parameter names).
- If any default is an instance of ast.List, ast.Dict, or ast.Set, return
  a Finding with:
    line  = the default's lineno
    rule  = "E002"
    message = f"mutable default argument in {node.name}"
- Return None if no mutable defaults are found.
- If there are MULTIPLE mutable defaults, return a Finding for the first one
  only (real linters deduplicate per function).

You also need a working rule_for decorator and a Linter class — copy your
solution from guided.py (or re-implement from scratch).

Hidden tests verify on multiple fixtures:
  - list default, dict default, set default each trigger
  - tuple/None/int defaults do NOT trigger
  - async functions with mutable defaults trigger
  - functions with no defaults return None
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
    """Decorator: register a rule for *node_type*."""
    raise NotImplementedError


# TODO: implement mutable_default_argument below and register it with
# @rule_for(ast.FunctionDef)


class Linter(ast.NodeVisitor):
    def __init__(self):
        self.findings: list[Finding] = []

    def visit(self, node: ast.AST):
        raise NotImplementedError

    def run(self, source: str) -> list[Finding]:
        tree = ast.parse(source)
        self.visit(tree)
        return sorted(self.findings, key=lambda f: f.line)
