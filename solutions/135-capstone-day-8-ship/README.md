---
day: 135-capstone-day-8-graduation
phase: phase-6-packaging-ast-capstone
module: capstone
style: story
---
# Capstone Day 8 — Graduation: real-world PR + friend-install

You published yesterday. That's not graduation. Graduation is when
*someone other than you uses the thing*. Two checks today, neither
optional. After both, you've shipped a tool, not finished a course.

## Today's deliverables (both required)

### 1. The friend-install check

Send the install command to one human you know:

> "Hey — I built a small Python linter for the bytelings capstone
> and I want to verify it installs cleanly on a machine that isn't
> mine. Could you run:
> 
> ```
> uv tool install <your-name>-lint
> <your-name>-lint .
> ```
> 
> in any Python project directory and tell me what happens? It
> should print findings (or nothing if your code is clean) and exit.
> 5 minutes max. Thanks."

Document their reply in your capstone repo's README. If it failed
on their machine (Python version too old, install permission, path
issue), you have *real software-shipping homework today* — fix it
and re-publish. Bump version to 0.1.1.

This step is what separates a "personal project" from a published
tool. The first install on someone else's machine will surface 1-2
things you couldn't have caught yourself.

### 2. The real-world PR

Pick one open-source Python repo. Small is fine — bigger isn't
better.

- Search GitHub: language=Python, stars > 50, < 5k LOC, recent
  commits. Avoid huge codebases (your linter is small; a big repo
  will drown it in findings).
- Run your linter on it. Pick **one** real finding — something
  that's genuinely a small bug or quality issue, not a stylistic
  nit you could argue either way.
- Open a PR with that single fix. The PR description should
  acknowledge the linter (if natural — don't be promotional, be
  technical):
  > "While running a small linter I'm building, I found a
  > `mutable-default-argument` here. The current code doesn't hit
  > the bug today (no callers retain the default), but switching to
  > `None`-then-init avoids the future trap."

Link the PR in your capstone README, regardless of merge outcome.
The point is "I opened a real PR upstream because of code I built,"
not "I got a PR merged."

## The graduation README

Update your project README with both artifacts:

```markdown
## Graduation log

- Friend-install verification: <Date>. <Friend's name> ran
  `uv tool install <your-name>-lint` on <macOS/Linux/Windows> and
  got <output summary or "clean exit">.
- Real-world PR: <link to PR>. Found a `mutable-default-argument`
  in <project name>. <Status: open / merged / closed>.
```

Commit this. Tag `v0.1.1` if you fixed any issues from the
friend-install. Push.

## What you just did

You built a tool from scratch in 8 days. It uses every concept from
the curriculum:

- **AST + visitor** (Module 26) — the spine of every rule
- **Packaging + console-scripts** (Module 25) — the wheel
- **Hash tables, scope stacks** (Modules 19) — unused-import
- **DFS** (Module 23) — the visitor's traversal
- **pyproject.toml + tomllib** (Module 25) — configuration
- **pytest fixtures** (Module 12) — your test suite
- **Strings deep + regex** (Module 2) — output formatting
- **Type hints** (Modules 1 + 8) — the public API
- **Refactoring as investigation** (Module 13) — every rule you
  added forced you to look at your visitor's shape

It's published. It's installable. Someone other than you ran it.
You opened a real PR with it. That's the package. That's
graduation.

## What's next (after the curriculum)

- **Use your linter on every Python project you touch for a year.**
  Real production wear is what tells you which rules actually help
  vs. which ones nag.
- **Add the rules YOU keep wishing existed.** That's how
  open-source maintenance starts.
- **Open issues on `astral-sh/ruff` or `pycqa/flake8`** when their
  rules don't match your taste. You now know the AST machinery; you
  can read those codebases. Some of those issues turn into PRs you
  can land.
- **Keep shipping.** You finished a 135-day curriculum. The point
  was never the curriculum — it was the capability. The capability
  is yours now.

## Now

Send that friend the install command. Pick that open-source repo.

You're ready.
