---
day: 128-capstone-day-1-pick-and-design
phase: phase-6-packaging-ast-capstone
module: capstone
style: story
---
# Capstone Day 1 — Pick your linter, design five rules

You've finished 127 days. The next 8 are different. There are no
ladder rungs. No hidden tests waiting. **One real thing, end-to-end,
shipped to PyPI under your name, with a download counter.** That's
graduation.

Today is design day. The default capstone project is **a tiny linter**.

## Why a linter

The linter is the one capstone shape that exercises every Phase-6
concept *and* parts of every earlier phase, while producing an
artifact a stranger can install and run:

| Concept | Where it lands in the linter |
|---|---|
| AST module + NodeVisitor (M26) | the spine — every rule visits AST nodes |
| Packaging + console-scripts (M25) | `<your-name>-lint` becomes a real `uv tool install` target |
| Dicts + scope stack (M19) | symbol table for the unused-import rule |
| DFS over AST (Phase 5) | the visitor IS depth-first traversal |
| pyproject.toml + tomllib (M25) | per-project rule configuration |
| Pytest fixtures (M12) | violation fixture files in `tests/fixtures/` |
| Strings deep + regex (M2) | message formatting and path normalization |

The artifact is undeniable. "I built a linter that's published,
installable, and run on a real open-source repo" is a CV line. "I
finished a curriculum" is not.

Full reference: see `docs/capstones/linter.md` for the complete spec,
day-by-day plan, and rule menu.

## Today's deliverable

By end-of-day you have:

1. **A project name.** Convention: `<yourgithub>-lint` or
   `<topic>-lint` (e.g. `pytier-lint`, `picky-lint`, `coverlint`).
   Pick something you're a little proud to type.
2. **A 5-rule shortlist** from the menu below. The minimum-viable bar
   is 5 distinct rules. Pick the ones you *understand the WHY of*,
   not the easiest to implement.
3. **A one-page design doc** in your scaffolded repo tomorrow:
   - The 5 rules in plain English
   - Output format (one line per finding: `path:line:col: rule-id: message`)
   - Configuration model (`[tool.<name>-lint]` in `pyproject.toml`)
   - Exit codes (0 if clean, 1 if findings)
4. **The visitor sketch.** One Python file with:
   ```python
   class Linter(ast.NodeVisitor):
       def __init__(self) -> None:
           self.findings: list[Finding] = []
       def visit_Try(self, node: ast.Try) -> None:
           # rule 1: bare-except — implement today
           ...
   ```
5. **Rule 1 end-to-end.** Pick the easiest rule on your shortlist
   (suggest: `bare-except`). Implement it, test on a fixture file
   you write, see one finding emit. Stop there.

## The rule menu (pick 5+)

Brief versions; full descriptions in `docs/capstones/linter.md`.

| Rule ID | Catches |
|---|---|
| `bare-except` | `except:` without an exception type |
| `mutable-default-argument` | `def f(x=[])` and friends |
| `unused-import` | `import os` never referenced (needs scope tracking) |
| `print-in-non-cli` | `print(...)` outside a `if __name__ == "__main__":` block |
| `function-too-long` | function body > N lines (configurable) |
| `class-with-only-static-methods` | "this should be a module" |
| `nested-loop-depth` | depth > N (configurable) |
| `single-letter-name` | `for i, j, k, l, m...` (excluding common cases) |

## Tomorrow

Day 129: scaffold the project (`uv init`), set up the test harness,
add 2 more rules.

## Final reminder before you start

The reason this capstone produces a *published* tool — not just "tests
pass" — is that "tests pass" is invisible the day after the curriculum
ends. A wheel on PyPI with one user other than you is the artifact
that proves you're a software engineer who ships, not a student who
finished a course.

You don't need 100 users. You need 1 friend who can run
`uv tool install <your-name>-lint && <your-name>-lint .` on their
codebase and see findings. Day 135 will check exactly that.
