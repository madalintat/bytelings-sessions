---
day: day-124-pyproject-and-deps
phase: phase-6-packaging-ast-capstone
module: module-25-packaging-with-uv
style: tour
---
# Day 124 — Read a real `pyproject.toml`

You've been typing `uv sync` for 123 days. Today you finally open the
file it's been reading. Here's a working `pyproject.toml` for a small
CLI tool. Read it line by line.

```toml
[project]
name = "habit-cli"
version = "0.1.0"
description = "Track tiny daily habits from the command line."
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "click>=8.1",
    "rich>=13.7",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "mypy>=1.10",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

Walk through it:

1. **`[project]`** — the standardized metadata table (PEP 621). Every
   modern Python tool reads this same shape. `pip`, `uv`, `poetry`,
   `hatch` — they all agree on these keys.
2. **`name`, `version`** — the package identity. Together they make
   `habit-cli==0.1.0`. Versions follow PEP 440 (`0.1.0`, `1.0.0a1`,
   `2.3.4.dev5`).
3. **`requires-python`** — a hard floor. `uv` will refuse to use a
   3.11 interpreter for this project. This is how you stop "works on
   my machine" before it starts.
4. **`dependencies`** — a list of PEP 508 requirement strings. `>=8.1`
   means "8.1 or newer." Use `~=` for "compatible release" (8.1 to
   <9.0). Pin loose, lock tight: this list stays loose, the
   `uv.lock` file pins exact versions for reproducibility.
5. **`[project.optional-dependencies]`** — extras that aren't installed
   by default. `uv sync --extra dev` pulls in `pytest` and `mypy` only
   when you ask for them.
6. **`[build-system]`** — only matters when you're *building* a wheel
   (Day 125). For pure-app projects you can ignore it; for libraries
   you'll publish, this names the backend that turns your source into
   a `.whl` file.

## What `uv` adds on top

`uv` invented two extra tables for ergonomics:

```toml
[tool.uv]
dev-dependencies = ["pytest>=8.0", "mypy>=1.10"]
```

`[tool.uv.dev-dependencies]` is a shortcut for "always install these in
the dev venv but never ship them." Effectively the same idea as the
`dev` extra above, just less typing for the common case.

`[tool.<name>]` is the standard escape hatch — every Python tool has
its own subtable here. `[tool.pytest.ini_options]`, `[tool.mypy]`,
`[tool.ruff]`. One file, many configs, no `setup.cfg` zoo.

## The lockfile, briefly

`pyproject.toml` says "I want click >= 8.1." `uv.lock` says "I picked
click 8.1.7 with this exact hash, and here's the resolved tree of
every transitive dep." You commit both. `uv sync` reads the lock and
reproduces the same install on every machine.

## Now: open `fluency.py`

You'll fix two broken bits of `pyproject.toml` parsing using
`tomllib` (stdlib in 3.11+). Tests expect plain dicts back.
