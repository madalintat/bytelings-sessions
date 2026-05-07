---
day: day-134-capstone-day-7-polish
phase: phase-6-packaging-ast-capstone
module: capstone
style: story
---
# Capstone Day 7 — Polish

Today is the day you make `habit` feel finished.

Open a fresh terminal. Type:

```bash
habit
```

What happens? On a good CLI tool, you get a friendly help message and
exit cleanly. On a half-finished one, you get a Python traceback or
an opaque "Usage: habit [OPTIONS] COMMAND" with no hint. Today we
make sure it's the former.

## The polish checklist

These are the things every shipped CLI tool does. Most of them are
five-line additions.

### 1. Logging instead of print debugging

You almost certainly have `print(f"loaded {len(habits)} habits")`
hiding somewhere from days 3-4. Replace with `logging.debug(...)`.
Wire up the root logger in `cli.py`:

```python
import logging

@click.group()
@click.option("-v", "--verbose", count=True, help="-v info, -vv debug")
def main(verbose: int) -> None:
    """Track tiny daily habits."""
    level = (logging.WARNING, logging.INFO, logging.DEBUG)[min(verbose, 2)]
    logging.basicConfig(level=level, format="%(levelname)s %(message)s")
```

Now `habit -v done meditate` shows info logs; `-vv` shows debug.

### 2. Friendlier errors

A user who types `habit reset typo` shouldn't see:

```text
Traceback (most recent call last):
  ...
KeyError: 'typo'
```

They should see:

```text
error: no habit named 'typo'
hint: try `habit list` to see your habits
```

Wrap the entry point. Catch known errors. Translate them to messages.
Click has `click.ClickException` for exactly this — raise it with a
message and click prints a clean error and exits non-zero.

### 3. Useful exit codes

`0` — success. `1` — runtime error (file not found, etc.). `2` —
usage error (bad args). Click already does `2` for you on bad args.
Make sure your `raise SystemExit(...)` calls use the right number.

### 4. `--help` for every subcommand

Click does most of this for free if you write good docstrings. Read
each one as a stranger would. "Mark <name> done for today." vs
"Records that you completed the habit today; auto-creates the habit
if it doesn't exist." The second is better.

### 5. The version flag

`habit --version` should print the version. You added
`@click.version_option()` on day 2 — confirm it reads from
`__version__` in `__init__.py`.

### 6. Empty-state and edge messages

What does `habit list` print when there are no habits? Today (day 4)
you wrote `(no habits yet — try habit done <name>)`. Good. Now check
each command for similar empty-state guidance.

### 7. `--quiet` for scripting

`habit done meditate --quiet` should print nothing on success (only
errors). Useful when piping or wrapping in cron.

## Concepts you're using

- **Logging (M14)** — `logging.basicConfig`, levels, the verbose flag
  pattern.
- **Errors / EAFP (M11)** — `try/except` at the boundary, raise
  `ClickException` with a useful message.
- **Click options vs flags (M5)** — `count=True` for `-v -vv`,
  `is_flag=True` for `--quiet`.
- **Reading your own code (M13)** — UX-driven editing.

## Today's deliverable

- [ ] `-v` and `-vv` work and change log output
- [ ] Every error path prints a helpful message (no raw tracebacks)
- [ ] Exit codes are deliberate (0, 1, 2)
- [ ] `--help` is well-written for every subcommand
- [ ] `--quiet` flag added (or document why you skipped it)
- [ ] Tests still green

The starter has the day 6 code with stubs marked `# polish:` where
you'd typically add these touches.

## A small luxury: `rich`

If you have time and want it, swap `click.echo` for `rich.print` in
the `list` and `recent` commands. Streak counts in green. Today's
column highlighted. It's fifteen minutes of work for a meaningful
quality bump. Optional — skip it if it'd push you into day 8 territory.

## Next

Tomorrow: ship. Build the wheel, write the README, install globally.
