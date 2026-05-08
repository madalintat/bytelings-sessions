---
day: 125-console-scripts-and-distribution
phase: phase-6-packaging-ast-capstone
module: module-25-packaging-with-uv
style: build-it
---
# Day 125 — Build the `console_scripts` mechanism yourself

Pretend Python doesn't have entry points. You wrote a CLI tool yesterday
called `pyproject-summary`. Right now your friend has to run it with:

```bash
uv run python apply.py pyproject.toml
```

You want them to type:

```bash
pyproject-summary pyproject.toml
```

How does that even work? There's no magic. A `console_script` is just a
**generated tiny shim file** placed on the user's `PATH`. When they
install your package, the build backend writes a file like this to
`~/.venv/bin/pyproject-summary`:

```python
#!/usr/bin/env python
import sys
from habit_cli.cli import main
sys.exit(main())
```

That's it. The shim imports `main` from your package and calls it. The
shebang makes it executable. The shell finds it on `PATH`. There is no
fourth thing.

## The pyproject side

You declare entry points in `pyproject.toml`:

```toml
[project.scripts]
pyproject-summary = "habit_cli.cli:main"
```

The string `"habit_cli.cli:main"` reads as: *import the module
`habit_cli.cli`, then call its attribute `main`.* The `:` is the
module-vs-attribute separator. This same `module:attr` notation shows
up in WSGI, Celery, click — once you see it, you see it everywhere.

## What `uv` does for you

When you run `uv pip install -e .` (editable install) or
`uv sync` in a project that defines its own scripts, `uv`:

1. Reads `[project.scripts]`.
2. For each entry, generates a shim in `.venv/bin/<name>`.
3. Marks it executable.

That's the whole "distribution" story for a pure-Python CLI. You don't
need PyPI to install your own tool. `uv tool install .` makes it
available globally without polluting any project's venv.

## Why a build backend at all?

`hatchling`, `setuptools`, `flit`, `poetry-core` — these are *build
backends*. Their job is to turn your source tree into a `.whl` file
(a zip with metadata) and a `.tar.gz` source distribution. The
backend writes the entry-point shims, copies your modules in, and
generates `METADATA`. You name your backend in `[build-system]`:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

You almost never run the backend by hand. `uv build` (or `python -m
build`) drives it for you. The output goes to `dist/`.

## Today's drill

You'll build a *fake* console-script generator. Given a
`{name: "module:attr"}` mapping, write the shim Python file as a
string. Then a tiny dispatcher that, given a parsed mapping and a
`sys.argv`, finds the right entry point and calls it.

This is exactly what `setuptools` does at install time — minus the
filesystem writes.

## Now: open `fluency.py`
