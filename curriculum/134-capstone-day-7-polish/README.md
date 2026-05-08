---
day: 134-capstone-day-7-publish
phase: phase-6-packaging-ast-capstone
module: capstone
style: story
---
# Capstone Day 7 — Publish to PyPI

The wheel exists. Today it goes public. By end-of-day, *anyone in
the world* can run `uv tool install <your-name>-lint` and get your
linter. That's the difference between "I made a thing" and "I
shipped a thing."

## Today's deliverables

1. **A PyPI account** at https://pypi.org/account/register/. Verify
   the email. (TestPyPI is a separate account at
   https://test.pypi.org if you want to rehearse.)
2. **An API token** for the project. Account settings → API tokens →
   "Add API token" → scoped to your project name (or "all projects"
   for the first publish, since the project doesn't exist yet).
3. **First publish to TestPyPI** (rehearsal — recommended):
   ```bash
   uv build              # produces dist/*.whl + dist/*.tar.gz
   uv publish --publish-url https://test.pypi.org/legacy/ \
              --token pypi-AgEI... 
   ```
4. **Verify TestPyPI install in a fresh dir**:
   ```bash
   cd /tmp && rm -rf verify && mkdir verify && cd verify
   uv tool install --index-url https://test.pypi.org/simple/ \
       --extra-index-url https://pypi.org/simple/ \
       <your-name>-lint
   <your-name>-lint --help
   ```
5. **Final publish to real PyPI**:
   ```bash
   uv publish --token pypi-AgEI...
   ```
6. **Verify real-PyPI install**:
   ```bash
   cd /tmp && rm -rf verify-real && mkdir verify-real && cd verify-real
   uv tool install <your-name>-lint    # ← from real PyPI now
   <your-name>-lint --help
   ```
7. **Tag the release in git**: `git tag v0.1.0 && git push origin v0.1.0`.

## The reality check

The first time you run `uv publish` it feels strange — you're
sending bytes to a server that anyone on Earth can install. Take
the moment. This is the artifact. Whatever happens after this day,
"I have a published Python package" is now true forever.

## What can go wrong (and how to fix it)

- **`HTTPError: 400 Client Error: Bad Request — name`**: someone
  already took your project name. Bump the name in pyproject.toml
  and rebuild. (You can squat your name now and never publish
  again, but the polite move is to pick something distinct.)
- **`HTTPError: 403 Forbidden`**: API token wrong or not scoped to
  this project. Re-issue.
- **Wheel uploads but install fails with `No matching distribution`**:
  Python version mismatch. Your `requires-python = ">=3.12"` excludes
  3.11 users. Check the install machine has 3.12+.
- **TestPyPI install fails with missing dependencies**: TestPyPI
  doesn't mirror real PyPI's deps. Use
  `--extra-index-url https://pypi.org/simple/` to fall back for any
  third-party deps. (If you kept `dependencies = []`, this won't bite.)

## Beyond the publish

Once it's published:

- **Watch the download counter.** PyPI publishes weekly stats with a
  delay. You'll see your first downloads (probably bots, that's fine).
  https://pypi.org/project/<your-name>-lint/
- **The page is editable**: visit your project page logged in,
  preview the README rendering, fix any markdown that broke.
- **Tag a `v0.1.0` git tag** if you haven't already. Source-of-truth
  for the version that's installable.

## Tomorrow

Day 135: real-world PR + friend-install check. The capstone graduates
when those two land.

## Now: ship

```bash
cd ~/code/<your-name>-lint
uv build
uv publish --token pypi-AgEI...     # ← read your token from your password manager
```

When it succeeds, sit with the moment. You're done with the hardest
day of the capstone.
