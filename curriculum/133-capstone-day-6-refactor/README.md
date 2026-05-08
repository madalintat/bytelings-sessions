---
day: 133-capstone-day-6-package
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 6 — Package the linter

Five days of code. Today it becomes a wheel that someone else can
install with one command. Most of the work is in `pyproject.toml`,
not Python.

## Today's deliverables

1. **Complete `pyproject.toml`** with metadata + console-script
   entrypoint.
2. **A built wheel** at `dist/<your-name>-lint-0.1.0-*.whl` from
   `uv build`.
3. **Local install verified**: `uv tool install --reinstall --from
   .` followed by `<your-name>-lint .` runs in a *fresh shell* and
   produces findings.
4. **A `LICENSE` file** (MIT is fine; check what you're comfortable
   with — this becomes a public artifact tomorrow).
5. **A `README.md` for the package** with: install command,
   minimum-config example, the rule list, and one
   findings-output screenshot.

## The pyproject.toml shape

```toml
[project]
name = "<your-name>-lint"
version = "0.1.0"
description = "A tiny opinionated linter — built as the bytelings capstone."
readme = "README.md"
requires-python = ">=3.12"
authors = [{name = "Your Name", email = "you@example.com"}]
license = {text = "MIT"}
keywords = ["linter", "ast", "static-analysis", "bytelings"]
classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Quality Assurance",
]
dependencies = []                    # ← stdlib only is the goal

[project.scripts]
<your-name>-lint = "<your_pkg>.cli:main"

[project.urls]
"Source" = "https://github.com/<you>/<your-name>-lint"
"Issues" = "https://github.com/<you>/<your-name>-lint/issues"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

The `[project.scripts]` line is the magic that turns
`<your-name>-lint .` into a real shell command after install.

## The fresh-shell verification

This is the bar. In a NEW terminal (so your dev environment doesn't
contaminate):

```bash
cd /tmp
uv tool install --reinstall --from ~/code/<your-name>-lint <your-name>-lint
which <your-name>-lint                         # ← prints a real path
<your-name>-lint --help                        # ← shows your CLI
<your-name>-lint ~/code/<your-name>-lint/src   # ← lints itself
```

The "lints itself" step is the dogfood test. Findings on your own
source are either real bugs to fix or false positives to fix
*before* you publish. You don't ship a linter that complains about
its own code.

## Stdlib-only is a feature

Read the `dependencies = []` line. Every dependency you add is a
download every user pays for. `tomllib`, `ast`, `pathlib`,
`fnmatch`, `dataclasses`, `argparse` (or `click` if you want the
nicer CLI) — these are all you need. Ship a thin tool.

## Common gotchas

- **Forgot `__init__.py`** in `src/<your_pkg>/` → wheel builds but
  the package is empty. Hatch's default layout requires it.
- **Console-script name has underscores when it should have hyphens**.
  By PyPI convention: hyphens in the `name` field, underscores in
  the import path. `picky-lint` ↔ `picky_lint`.
- **Forgot to bump version on rebuild** → uv tool install thinks
  you've already got the latest. Bump `version = "0.1.1"` between
  iterations.

## Tomorrow

Day 134: publish to PyPI. Account, twine, the actual upload, and
the verification install from PyPI itself (not from your local dir).

## Now: code

```bash
cd ~/code/<your-name>-lint
uv build
uv tool install --reinstall --from . <your-name>-lint
<your-name>-lint .
```

If that produces output that looks like a linter and exits with the
right code, you're ready for tomorrow.
