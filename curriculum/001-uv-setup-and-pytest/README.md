---
day: day-001-uv-setup-and-pytest
phase: phase-1-python-core
module: module-01-setup-and-values
style: story
---
# Day 1 — Your first morning at the new repo

It's Monday, 9 AM. You've been hired to maintain a small Python tool.
You clone the repo, open the README, and see one line:

> `uv sync && uv run pytest`

You don't know what `uv` is yet. You don't have to. The repo's lockfile
pins everything you need. Type the command. Watch it work.

```text
$ uv sync
Installed 12 packages in 240ms
$ uv run pytest
====== 14 passed in 0.31s ======
```

That's it. You're now running the same Python, same pytest, same exact
package versions as everyone else who works on this code. No "works on
my machine." That problem just stopped existing.

## What `uv` actually does

`uv` is a Python package manager and venv tool. Think of it as the
glue between three things:

1. **A venv** — an isolated Python install, so this project doesn't
   poison your laptop's other Python projects.
2. **A lockfile** — a precise record of every package version, so
   "the deps that worked yesterday" is reproducible forever.
3. **A runner** — `uv run <thing>` makes sure `<thing>` uses *this*
   project's venv automatically. No `source venv/bin/activate` ritual.

For this whole curriculum, you'll use `bytelings` (the watcher) to
drive your day. It runs the right tests for the rung you're on,
every time you save.

## Rung 1: run `uv sync`

That's literally it. Open a terminal in this folder and run:

```bash
uv sync
```

Now in *another* terminal (or split pane), start the watcher:

```bash
bytelings
```

The watcher will see your `.venv`, mark Rung 1 done, and move you
straight to Rung 2.

> If you start the watcher *before* `uv sync`, it'll wait for you
> and pick up the `.venv` the moment it appears. No restart needed.

## Then: open `02_fluency.py`

You'll fix two tiny things. The watcher will tell you when they're
right. Don't worry — you can't break anything.
