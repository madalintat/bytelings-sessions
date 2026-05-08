---
day: day-135-capstone-day-8-ship
phase: phase-6-packaging-ast-capstone
module: capstone
style: story
---
# Capstone Day 8 — Ship

Day 135. The last day. Today you build the wheel, install the tool
globally, and write the README.

## What "ship" means here

You don't have to publish to PyPI. (You can if you want — the steps
are at the end.) "Shipping" for this curriculum means:

1. The package builds. `uv build` produces `dist/habit-0.1.0.whl`
   without errors.
2. The tool installs globally with one command.
3. There's a README that someone could read in 60 seconds and know
   what your tool does, how to install it, and how to use it.
4. You can git-clone the repo on a fresh machine, run two commands,
   and have a working tool.

## Step 1 — Build the wheel

```bash
uv build
```

Output:

```text
Building source distribution...
Building wheel...
Successfully built dist/habit-0.1.0.tar.gz
Successfully built dist/habit-0.1.0-py3-none-any.whl
```

A wheel (`.whl`) is a zip file with a specific structure. You can
literally `unzip dist/habit-0.1.0-py3-none-any.whl -d /tmp/look` and
poke around. You'll see your `habit/` package, a `METADATA` file
with everything from your `pyproject.toml`, and a `RECORD` file with
hashes of every file shipped.

## Step 2 — Install globally

```bash
uv tool install .
```

This puts `habit` on your `PATH`. From any directory, in any shell,
you type `habit list` and it works. `uv tool` keeps each installed
tool in its own venv so they don't fight.

To uninstall later: `uv tool uninstall habit`.

## Step 3 — Write the README

Put a `README.md` next to your `pyproject.toml`. The shape that works:

```markdown
# habit

Track tiny daily habits from the command line. Single JSON file,
zero dependencies you don't already have.

## Install

    uv tool install habit

## Use

    habit done meditate         # mark today done
    habit list                  # see streaks
    habit list --sort streak    # longest streaks first
    habit recent                # last 14 days as a grid
    habit reset meditate --yes  # wipe one habit

Data lives in `~/.config/habit/data.json`. Override with `HABIT_DATA`.

## Why

I wanted a habit tracker that lives in my terminal next to git, not in
a separate app. So I wrote one in 8 days.
```

That's the entire README. Short. Useful. Done. **Don't** put a
"Contributing" section, a code-of-conduct link, or a roadmap. This is
your tool. If you change your mind about the format next week, you'll
edit the JSON by hand.

## Step 4 — Commit and push

```bash
git add .
git commit -m "ship habit v0.1.0"
git push
```

Now anyone with your repo URL can:

```bash
git clone <your-repo>
cd habit
uv tool install .
```

That's the whole shipping story for a personal tool.

## Optional: publish to PyPI

If you want strangers to be able to `uv tool install habit-yourname`:

```bash
# Register on https://pypi.org first.
uv publish
```

You'll need to pick a unique name (`habit` is taken — try
`habit-yourname` or `habits-cli`). Update `[project].name` in
`pyproject.toml`, rebuild, then publish.

For most personal tools, **the git repo is the distribution**. You
don't need PyPI to ship.

## Concepts you're using today

- **Packaging (M25)** — `uv build`, the wheel format, install entry
  points.
- **Reading docs (M13)** — your README is documentation; write it
  the way you wish other tools wrote theirs.
- **Versioning** — bump `__version__` to `0.1.0` if you haven't.
  When you change something, bump it.

## Today's deliverable

- [ ] `uv build` produces a `.whl` file
- [ ] `uv tool install .` succeeds; `habit --help` works in any dir
- [ ] `README.md` exists and answers what/install/use
- [ ] `__version__` is `0.1.0` (or whatever you settled on)
- [ ] Tests still pass
- [ ] Final commit pushed

The starter has the day 7 code plus a `README.md` template.

## What's next (after the curriculum)

You finished. Take a moment.

The skills you built across 135 days don't expire. The instinct to
reach for a generator instead of a list, the habit of `try/except` at
the boundary, the AST you can now read — those don't go away.

Pick something *new* to build with them. A second tool. A
contribution to an open-source project. A rewrite of something at
work that's been bothering you. Whatever it is — shorter than 135
days. Use what you've got.
