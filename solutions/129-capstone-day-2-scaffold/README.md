---
day: 129-capstone-day-2-scaffold
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 2 — Scaffold + 2 more rules

Yesterday: project name, 5-rule shortlist, design doc, `bare-except`
end-to-end. Today: a real Python package skeleton + two more rules
running in tests.

## Today's deliverables

By end-of-day:

1. **A `uv init` project** at `~/code/<your-name>-lint/` (or wherever
   you keep work):
   ```
   <your-name>-lint/
     pyproject.toml
     src/<your_pkg>/
       __init__.py
       linter.py             ← Linter(ast.NodeVisitor) lives here
       rules.py              ← @register-decorated rule functions
       cli.py                ← console-script entrypoint
     tests/
       fixtures/             ← intentionally-violating .py files
       test_rules.py
   ```

2. **Test harness wired up**: `pytest` runs from repo root, finds
   `tests/`, fails on any rule that doesn't catch its fixture.

3. **Two more rules implemented + tested**: pick from yesterday's
   shortlist. Suggested for today: `mutable-default-argument` and
   `function-too-long`.

4. **A fixture file per rule**: `tests/fixtures/bare_except.py`,
   `tests/fixtures/mutable_default.py`, etc. Each contains exactly
   one violation of its rule (and nothing else, so a false positive
   is easy to spot).

## The rule-registration pattern (use this)

Single visitor, dispatch by AST node type, rules opt in:

```python
# rules.py
import ast
from typing import Callable

_REGISTRY: dict[type, list[Callable]] = {}

def rule_for(node_type: type):
    def decorator(fn):
        _REGISTRY.setdefault(node_type, []).append(fn)
        return fn
    return decorator

@rule_for(ast.Try)
def bare_except(node: ast.Try, ctx) -> None:
    for handler in node.handlers:
        if handler.type is None:
            ctx.findings.append(Finding(handler, "bare-except",
                "use `except <ExceptionType>:` not bare `except:`"))

@rule_for(ast.FunctionDef)
def mutable_default(node: ast.FunctionDef, ctx) -> None:
    for default in node.args.defaults:
        if isinstance(default, (ast.List, ast.Dict, ast.Set)):
            ctx.findings.append(Finding(default, "mutable-default-argument",
                "default arg is mutable; use None and create inside"))
```

The Linter visitor's job becomes a 5-line dispatch:

```python
class Linter(ast.NodeVisitor):
    def __init__(self) -> None:
        self.findings: list[Finding] = []
    def visit(self, node: ast.AST) -> None:
        for rule_fn in _REGISTRY.get(type(node), []):
            rule_fn(node, self)
        self.generic_visit(node)
```

## What "tested" means

For each rule, two test shapes:

```python
def test_bare_except_flags_the_violation():
    findings = run_linter(FIXTURE_DIR / "bare_except.py")
    assert any(f.rule == "bare-except" for f in findings)

def test_bare_except_does_not_false_positive():
    findings = run_linter(FIXTURE_DIR / "no_violations.py")
    assert not any(f.rule == "bare-except" for f in findings)
```

The second test (no false positives on a clean file) is the one
beginners skip and the one that matters most.

## Reference

`docs/capstones/linter.md` has the full rule menu, AST-node hints
per rule, and the day-by-day plan you're following.

## Tomorrow

Day 130: hit the 5-rule minimum. Refactor the visitor if needed.

## Now: code

Open your editor. The `Patterns: P-30 (ast-walker-visitor)` line is
your daily compass — every rule visits AST nodes. Print
`bytelings patterns P-30` if you want the canonical example fresh
in your head before you start.
