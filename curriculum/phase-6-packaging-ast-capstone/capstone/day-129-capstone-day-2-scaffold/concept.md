---
day: day-129-capstone-day-2-scaffold
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 2 — Scaffold the project

You have a design. Today you create the bones: a `pyproject.toml`,
a `src/` layout, an empty CLI entry point that runs and prints help.
By tonight you'll be able to type:

```bash
uv run habit --help
```

and see your tool respond. No real functionality yet — that's days 3-4.

## What you're building (concrete)

A standard `src/` layout package:

```text
day-129-capstone-day-2-scaffold/
├── pyproject.toml          # name, version, deps, [project.scripts]
├── src/
│   └── habit/
│       ├── __init__.py     # __version__ = "0.1.0"
│       ├── cli.py          # def main() -> int: parses args, prints help
│       ├── core.py         # empty stub for tomorrow's logic
│       └── storage.py      # empty stub for JSON load/save
└── tests/
    └── test_cli.py         # confirms `--help` runs and exits 0
```

The `src/` layout matters. It forces you to install your package
(even just editably with `uv sync`) before tests can import it. That
catches "tests pass because they accidentally imported the dev tree"
bugs early.

## pyproject.toml — the minimum

```toml
[project]
name = "habit"
version = "0.1.0"
description = "Track tiny daily habits."
requires-python = ">=3.12"
dependencies = ["click>=8.1"]

[project.scripts]
habit = "habit.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/habit"]
```

The `[tool.hatch.build.targets.wheel]` line tells hatchling where the
package lives — it's needed because the package is in `src/habit`,
not `./habit`. Without it the wheel would be empty.

## The CLI shell

`cli.py` for today is just enough to be a real command:

```python
import click

@click.group()
@click.version_option()
def main():
    """Track tiny daily habits."""

@main.command()
def list():
    """List all habits and their streaks."""
    click.echo("(no habits yet — try `habit done <name>`)")
```

You add a `done` and `reset` placeholder too, both printing "TODO".
Real behavior arrives tomorrow.

## Substituting your own project?

The scaffold is the same. Rename `habit` to whatever you picked.
Adjust dependencies in `[project]` (drop `click` if you'd rather use
`argparse`; add `rich` if you want pretty output). Keep `src/`
layout, keep one `[project.scripts]` entry.

## Today's deliverable

When you're done:

- [ ] `uv sync` succeeds (it'll install your local package)
- [ ] `uv run habit --help` prints help text
- [ ] `uv run habit list` prints something
- [ ] `uv run pytest tests/` passes (the help-runs test below)

The starter files are real, working code. They are what you'd write
yourself. You'll edit them — and tomorrow you'll start replacing the
TODOs with real logic.

## Next

Tomorrow: build the storage layer + the `done` command. By tomorrow
night, `habit done meditate` will actually save something to disk.
