---
day: 132-capstone-day-5-output-and-ci
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 5 — Output formatting + exit codes + CI

Your linter knows what's wrong but doesn't yet *talk* like a real
tool. Today: the wire format, exit codes, sort order, and a sketch
of CI integration. The format is what makes a linter scriptable;
the exit code is what makes it `&&`-able.

## The wire format

One finding per line, sorted by `(path, line, col)`:

```
src/foo.py:12:8: bare-except: use `except <ExceptionType>:` not bare `except:`
src/foo.py:34:0: function-too-long: function `process_orders` is 73 lines (max 50)
tests/test_bar.py:5:4: print-in-non-cli: print outside a __main__ block
```

This format isn't arbitrary — it's a de facto standard since Unix
`grep` ate the world. Any editor or CI that recognizes "filename
colon line colon col" will jump-to-finding for free. ruff, flake8,
mypy, pylint, eslint — they all emit this shape.

## The implementation

```python
def format_finding(f: Finding) -> str:
    return f"{f.path}:{f.line}:{f.col}: {f.rule_id}: {f.message}"

def main(args: list[str]) -> int:
    targets = expand_targets(args)
    config = load_config(repo_root_for(targets), TOOL_NAME)
    all_findings: list[Finding] = []
    for path in targets:
        if any(fnmatch.fnmatch(str(path), p) for p in config["exclude"]):
            continue
        all_findings.extend(lint_file(path, config))
    all_findings.sort(key=lambda f: (str(f.path), f.line, f.col))
    for f in all_findings:
        print(format_finding(f))
    return 1 if all_findings else 0
```

## Exit codes

```
0   no findings (clean)
1   one or more findings
2   usage error (bad CLI args, file not found, …)
```

The 0/1 split is the contract every CI tool reads. `<your-name>-lint
src/ && pytest && deploy` works because of these three integers.

`raise click.UsageError(...)` exits with 2; click handles it.

## Path normalization

A finding emitted with a relative path that doesn't match where the
user invoked from will confuse editor jump-to-line. Normalize:

```python
def to_cwd_relative(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(Path.cwd()))
    except ValueError:
        return str(p)
```

If the file is outside cwd, fall back to the absolute path. Editors
handle both.

## Today's deliverables

1. **Format output** as above. Every finding parses cleanly with a
   regex like `r"^(.+?):(\d+):(\d+): ([a-z-]+): (.+)$"`.
2. **Sort** by `(path, line, col)`. Stable order is essential for CI
   diffing.
3. **Exit codes** wired up (return 0/1 from `main`, `sys.exit(rc)`
   in the console-script entrypoint).
4. **A README sketch of CI integration**:
   ```yaml
   # .github/workflows/lint.yml
   - name: Run <your-name>-lint
     run: uv tool run --from . <your-name>-lint src/
   ```
5. **Tests for sorted output**: feed two files with findings in
   reverse-discovery order; assert output is sorted by path.

## Tomorrow

Day 133: package. `pyproject.toml` `[project.scripts]`. Wheel
build. Local install via `uv tool install --from .`.

## Stretch

- A `--format=json` flag that emits JSONL. Editors consuming machine
  output will love you.
- A `--diff-only` mode that lints only files changed against
  `origin/main`. (Use `git diff --name-only origin/main`.)
- Pretty colored output for TTY (`rich`?). Skip the colors when
  piped — `sys.stdout.isatty()`.

## Now: code
