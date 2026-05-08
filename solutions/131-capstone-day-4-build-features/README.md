---
day: 131-capstone-day-4-configurability
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 4 — Make the linter configurable

A linter without configuration is a linter nobody adopts. Half the
work of a real tool is letting users say "yes use these rules but
not THAT one, and bump function-too-long-max to 30 because we like
small functions here."

## Today's deliverables

1. **Read `pyproject.toml`** from the target project's root via
   `tomllib`. Look for `[tool.<your-name>-lint]`.
2. **Honor a `rules` allowlist.** Default is "all rules"; if the
   user supplied `rules = ["bare-except", "unused-import"]`, only
   those run.
3. **Honor per-rule thresholds.** At minimum:
   - `function-too-long-max` (int, default 50)
   - `nested-loop-depth-max` (int, default 3) — only if you
     implemented that rule
4. **An `exclude` glob list** (default empty) that filters paths
   before linting.
5. **Tests for the config layer.** A fixture `pyproject.toml` with
   a non-default config; a test that runs the linter and checks
   the right rules ran with the right thresholds.

## The tomllib pattern

```python
import tomllib
from pathlib import Path

DEFAULTS = {
    "rules": None,                   # None = all
    "function-too-long-max": 50,
    "nested-loop-depth-max": 3,
    "exclude": [],
}

def load_config(target_root: Path, tool_name: str) -> dict:
    pyproject = target_root / "pyproject.toml"
    if not pyproject.is_file():
        return dict(DEFAULTS)
    data = tomllib.loads(pyproject.read_text())
    user = data.get("tool", {}).get(tool_name, {})
    return {**DEFAULTS, **user}
```

That's the entire implementation. tomllib is stdlib in Python 3.11+,
no third-party dep needed.

## Threading the config through

Each rule needs the config to look up its threshold:

```python
@rule_for(ast.FunctionDef)
def function_too_long(node, ctx):
    body = node.body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        body = body[1:]      # skip docstring
    if not body:
        return
    line_count = (body[-1].end_lineno or body[-1].lineno) - body[0].lineno + 1
    if line_count > ctx.config["function-too-long-max"]:
        ctx.findings.append(Finding(node, "function-too-long",
            f"function `{node.name}` is {line_count} lines (max {ctx.config['function-too-long-max']})"))
```

The visitor's `ctx` carries `findings` (Day 129) and `config`
(today). Two pieces of context, threaded uniformly.

## The `rules` allowlist mechanics

Easiest approach: filter at registration-call time, not at
registration time.

```python
def lint_file(path: Path, config: dict) -> list[Finding]:
    tree = ast.parse(path.read_text())
    visitor = Linter(config)
    visitor.visit(tree)
    findings = visitor.findings
    findings.extend(rule(tree) for rule in WHOLE_MODULE_RULES)
    if config["rules"] is not None:
        allowlist = set(config["rules"])
        findings = [f for f in findings if f.rule_id in allowlist]
    return findings
```

A post-filter is wasteful (computes findings just to throw them
away) but simple. A registration-time filter is faster but adds
complexity. For a linter running on ~hundreds of files at a time,
the wasted work is negligible. Ship the simple version.

## Tomorrow

Day 132: output formatting. `path:line:col: rule-id: message`. Sort.
Exit codes. The CI integration story.

## Stretch

- Per-file inline overrides via `# noqa: rule-id` comments. Real
  linters do this; it's ~20 lines of source-line-comment parsing.
- `--rules` and `--exclude` CLI flags that override pyproject.

## Now: code
