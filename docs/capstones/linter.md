# Capstone: a tiny published linter (Days 128–135)

The default bytelings capstone. Eight days, one artifact, one PyPI
publish, one friend's machine the wheel is installable on. The
detailed reference for every capstone day's README.

## Goal

Ship `<your-name>-lint`: a Python linter with at least 5 distinct
rules, packaged, tested, published to PyPI under your account,
installable via `uv tool install <your-name>-lint`, and run on a real
open-source repo with one PR opened upstream fixing one finding.

## Minimum viable scope (the bar to pass)

A learner has SHIPPED the capstone iff:

- [ ] Wheel published to PyPI (TestPyPI is OK if regular PyPI declines)
- [ ] At least **5 distinct rules** active and tested
- [ ] Each rule has at least one **violation fixture** in `tests/fixtures/`
- [ ] Configurable via `[tool.<name>-lint]` in a target's `pyproject.toml`
- [ ] Reads file via `ast.parse`, walks via `ast.NodeVisitor`
- [ ] Exit code 0 if clean, 1 if findings
- [ ] One **friend's machine** ran `uv tool install <name>-lint` successfully
- [ ] One **real PR** opened against an open-source repo fixing a real finding,
      linked from the capstone README

## The rule menu

Each rule has: an ID (kebab-case), what it catches, what AST node(s)
it visits, and one example violation.

### `bare-except`
Catches `except:` (no exception type). Visits `ast.ExceptHandler`.
```python
try: risky()
except:           # ← bare-except: should be `except SomeException:`
    pass
```

### `mutable-default-argument`
Catches `def fn(arg=[])`, `def fn(arg={})`, `def fn(arg=set())`.
Visits `ast.FunctionDef`, inspects `args.defaults`.
```python
def append(item, into=[]):     # ← persistent state surprise
    into.append(item)
    return into
```

### `unused-import`
Catches imports never referenced. Needs a **scope-stack symbol
table**: a list-of-dicts where each scope's dict maps name → ast.Import
node. On scope exit, any unconsumed name is a violation.

```python
import os         # ← unused-import: not referenced anywhere below
def main(): print("hello")
```

### `print-in-non-cli`
Catches `print(...)` outside a `if __name__ == "__main__":` block.
Track depth-of-main-guard via the visitor stack. Visits `ast.Call`.
```python
def helper():
    print(x)      # ← print-in-non-cli: not in a __main__ block
```

### `function-too-long`
Configurable threshold (default 50 body lines). Visits `ast.FunctionDef`.
Body line count = `node.end_lineno - body[0].lineno + 1` (excluding
the docstring node if present).

### `class-with-only-static-methods`
Visits `ast.ClassDef`. If every method is decorated `@staticmethod`,
emit "this should be a module."

### `nested-loop-depth`
Configurable threshold (default 3). Track loop nesting in a counter
that's incremented on `visit_For` / `visit_While` and decremented on
exit (use `generic_visit` and a try/finally).

### `single-letter-name`
Visits `ast.Name` and `ast.arg`. Excludes the common-case allowlist
(`i`, `j`, `k`, `n`, `m`, `x`, `y`, `_`, `T` for TypeVar).

## Output format

One finding per line:
```
path:line:col: rule-id: human-readable message
```

Sorted by `(path, line, col)`. Print to stdout. Errors (file not
found, syntax error in target) go to stderr with non-zero exit.

## Configuration

Read `[tool.<name>-lint]` from the target project's `pyproject.toml`.
Keys:
- `rules` — list[str] of rule IDs to enable (default: all)
- `function-too-long-max` — int (default 50)
- `nested-loop-depth-max` — int (default 3)
- `exclude` — list[str] of glob patterns

```toml
[tool.picky-lint]
rules = ["bare-except", "unused-import", "function-too-long"]
function-too-long-max = 30
exclude = ["tests/**", "vendor/**"]
```

## Day-by-day

### Day 128 — Pick + design
Project name. Rule shortlist (5+ from menu). Visitor sketch. One
rule end-to-end (`bare-except`).

### Day 129 — Scaffold + 2 more rules
`uv init`. Test harness (`pytest`, `tests/fixtures/`). Implement
`mutable-default-argument` and `function-too-long`. Each ships with
a fixture file demonstrating one violation.

### Day 130 — Hit the 5-rule minimum
Implement two more rules. Refactor visitor: each rule is a
`@register("rule-id")` method, the visitor dispatches by AST node
type. Strip duplication.

### Day 131 — Configurability
`tomllib.load(open("pyproject.toml", "rb"))`. Read `[tool.<name>-lint]`.
Apply rule allowlist + thresholds. Default-when-missing path.

### Day 132 — Output formatting + exit codes
Sort findings. Format `path:line:col: rule-id: message`. Exit 0/1.
CI integration sketch: `<name>-lint . --fail-on-finding` works as a
GitHub Action step.

### Day 133 — Package
Author `pyproject.toml` with `[project.scripts]` console-script entry.
Build wheel. Test `uv tool install --from . <name>-lint` on your own
machine.

### Day 134 — Publish to PyPI
`uv build`. Account on PyPI (real or TestPyPI). `twine upload`. Verify
fresh `uv tool install <name>-lint` in a clean dir installs from PyPI.

### Day 135 — Real-world PR + friend-install check
Pick a small open-source Python repo. Run your linter. Find one real
finding. Open a PR upstream. Link in your capstone README.

Send your wheel to a friend. They run
`uv tool install <name>-lint && <name>-lint <some-codebase>` and tell
you it worked. Document that in the capstone README.

## Choice menu — alternative capstones

If a linter doesn't fit the learner's interest, three pre-vetted
alternatives that meet the same "shipped, published, friend-installable"
bar:

- `<name>-toc` — markdown TOC inserter (parses markdown AST instead
  of Python AST). Same packaging shape.
- `<name>-linkcheck` — async link checker for a website. Tests
  Phase-2 async + Phase-3 logging.
- `<name>-logslice` — log-file query CLI. Tests strings deep + dicts
  + files.

Each has its own sub-doc in `docs/capstones/` (TODO — author when a
learner picks one).

## Why this shape

Karpathy's "Neural Networks: Zero to Hero" capstone is an actual GPT
the student trained, with weights they can show. bytelings' linter
is the equivalent: an actual tool other developers can install, with
a download counter and a real-world PR.

"Tests pass" is invisible the day after the curriculum ends. A wheel
on PyPI with 3 downloads from strangers is the artifact that
graduates a software engineer.
