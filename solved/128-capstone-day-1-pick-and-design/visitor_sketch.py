"""Day 128 — Capstone Day 1: visitor sketch + bare-except rule (Rule 1).

This file is the deliverable for Day 128's 'visitor sketch' and
'Rule 1 end-to-end' tasks.  It implements only the bare-except rule;
all other rules are stubs to be filled on Days 129–134.

Output format (one line per finding):
    path:line:col: rule-id: message

Exit codes: 0 if clean, 1 if findings.

The bare-except rule fires when an `except:` clause names no exception
type.  In the AST this appears as an ExceptHandler whose `type` attribute
is None.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    path: str
    line: int
    col: int
    rule: str
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}:{self.col}: {self.rule}: {self.message}"


# ---------------------------------------------------------------------------
# Linter visitor
# ---------------------------------------------------------------------------

class Linter(ast.NodeVisitor):
    """AST visitor that collects rule violations."""

    def __init__(self, path: str = "<string>") -> None:
        self.path = path
        self.findings: list[Finding] = []

    # Rule: bare-except (no exception type specified)
    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        if node.type is None:
            self.findings.append(
                Finding(
                    path=self.path,
                    line=node.lineno,
                    col=node.col_offset,
                    rule="bare-except",
                    message="bare `except:` catches everything — name an exception type",
                )
            )
        self.generic_visit(node)

    # Stub placeholders — to be implemented Days 129-134
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        # Rule stubs: mutable-default-argument, function-too-long
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef  # type: ignore[assignment]

    def visit_Import(self, node: ast.Import) -> None:
        # Rule stub: unused-import
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        # Rule stub: unused-import
        self.generic_visit(node)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def lint_source(source: str, path: str = "<string>") -> list[Finding]:
    """Parse *source* and return all findings."""
    tree = ast.parse(source, filename=path)
    visitor = Linter(path=path)
    visitor.visit(tree)
    return visitor.findings


# ---------------------------------------------------------------------------
# Quick smoke test (run as script)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _FIXTURE = """\
try:
    pass
except:
    print("oops")

try:
    pass
except ValueError:
    print("specific — fine")
"""
    findings = lint_source(_FIXTURE, path="fixture.py")
    for f in findings:
        print(f)
    print(f"\n{len(findings)} finding(s)")
