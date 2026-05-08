---
day: 130-capstone-day-3-build-core
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 3 — Hit the 5-rule minimum

Day 1: design + bare-except. Day 2: scaffold + 2 more. Today: get to
**5 distinct, tested rules** — the minimum-viable bar from the
capstone spec.

## Today's deliverables

1. **Two more rules implemented**, each with a fixture file and the
   two-test pair (flags-violation + no-false-positive). Total
   active rules: 5+.
2. **Refactor the visitor** if it's grown messy. Each rule should be
   a single `@rule_for(...)` function. If you've started branching
   inside a rule for sub-cases, split into two registered rules.
3. **A `Finding` dataclass** that captures everything needed for
   tomorrow's output formatting (path, line, col, rule_id, message).

## Pick the next two rules carefully

Some rules are easy (`bare-except`, `mutable-default-argument`,
`function-too-long`). Some are hard (`unused-import`, which needs a
**scope stack**). For Day 3 the right pick is one of each:

- **One easy**: `print-in-non-cli` or `class-with-only-static-methods`
  or `single-letter-name`. Each is one AST-node type, no state.
- **One stateful**: `unused-import`. This one EARNS its difficulty
  because it requires the scope-stack pattern that real linters use.

## The unused-import rule (worked example)

You can't just visit `ast.Import` and complain — you need to know
whether the imported names are used *anywhere in the same module*.
That's a two-pass walk:

```python
class UnusedImportRule:
    def __init__(self) -> None:
        self.imported: dict[str, ast.AST] = {}    # name → import node
        self.used: set[str] = set()

    def collect_imports(self, tree: ast.AST) -> None:
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname or alias.name.split(".")[0]
                    self.imported[name] = node
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    name = alias.asname or alias.name
                    self.imported[name] = node

    def collect_uses(self, tree: ast.AST) -> None:
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                self.used.add(node.id)
            elif isinstance(node, ast.Attribute):
                # `os.path` uses `os`. Walk to the base.
                base = node
                while isinstance(base, ast.Attribute):
                    base = base.value
                if isinstance(base, ast.Name):
                    self.used.add(base.id)

    def findings(self) -> list[Finding]:
        return [
            Finding(node, "unused-import", f"`{name}` imported but never used")
            for name, node in self.imported.items()
            if name not in self.used
        ]
```

Two passes is fine; the file is already in memory as the AST. You
get scope-correct results without writing a full scope-stack
analyzer (which is overkill for module-level imports).

## The visitor refactor

If your `Linter` class has grown 10+ `visit_X` methods, the registry
pattern from Day 129 pays off now. Re-look at `_REGISTRY` and
extract every `visit_X` into a `@rule_for(ast.X)` function.
Whole-module rules (like unused-import) live OUTSIDE the visitor
and run after a single `ast.walk(tree)` pass.

```python
def lint_file(path: Path) -> list[Finding]:
    tree = ast.parse(path.read_text())
    findings: list[Finding] = []
    # node-level rules via the visitor
    visitor = Linter()
    visitor.visit(tree)
    findings.extend(visitor.findings)
    # whole-module rules
    for whole_module_rule in WHOLE_MODULE_RULES:
        findings.extend(whole_module_rule(tree))
    return findings
```

## Tomorrow

Day 131: configurability. `pyproject.toml [tool.<name>-lint]`
reading via `tomllib`. Per-rule allowlist, per-rule thresholds.

## Stretch (only if you finish early)

- Add line numbers to `Finding`. AST nodes carry `node.lineno` and
  `node.col_offset` natively.
- Try running your linter on its own source. The dogfood pass.
  Document any findings (real or false positive) in a TODO list —
  Day 133 will help you fix the false positives before publishing.

## Now: code
