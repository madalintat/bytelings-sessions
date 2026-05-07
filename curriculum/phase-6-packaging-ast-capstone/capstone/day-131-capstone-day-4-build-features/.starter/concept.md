---
day: day-131-capstone-day-4-build-features
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 4 — Add the next two features

Yesterday: `done`, `list`, and storage. Today you flesh out the rest:
`reset`, `recent`, and a richer `list`. By tonight `habit` should
feel like a complete tiny tool — the kind you'd actually paste into
your dotfiles.

## Today's three features

1. **`habit reset <name>`** — wipe a habit's log (or delete the habit
   entirely; pick one and stay consistent). Add a `--yes` flag for
   non-interactive use; otherwise prompt to confirm.
2. **`habit recent [--days N]`** — print the last N days as a
   tiny calendar grid. Default N=14. Shows which days each habit
   was done. Sketch:

   ```text
   meditate    . . X X . X X . X X X X X X
   read        X X X X . . . . . . . . . .
                Tu W  Th F  Sa Su M Tu W  Th F  Sa Su M
   ```

3. **`habit list --sort streak|name`** — let the user pick how to
   sort. Default is alphabetical; `--sort streak` puts longest
   streaks first.

## Concepts you're using today

- **Click subcommands + options** (M5 + M25) — the verbs are click
  commands, the flags are click options.
- **Comprehensions / generators** (M6) — for filtering recent dates.
- **`itertools`** (M6) — `itertools.takewhile` is gorgeous for
  streak-walking. Re-implement `streak()` with it if you're feeling
  fancy.
- **Sorting with key** (M5/M21) — `sorted(habits.values(),
  key=lambda h: -h.streak(today))` for streak-first.
- **Dates + `timedelta`** (stdlib) — `date.today() - timedelta(days=n)`.

## A note on UX

You're the user too. After you implement each feature, *use it*.

If `habit reset meditate` makes you nervous because there's no undo
prompt — add a prompt. If `habit recent` is unreadable — change the
formatting. The whole point of building your own tools is the
feedback loop on UX is *you*.

If you're stuck on what to print: copy what `git status` does. Short
header, list of items, blank line, footer hint. Boring is good.

## Composition over copy-paste

Two things in `core.py` you'll likely add today:

```python
def filter_log(habit: Habit, since: date) -> list[date]:
    """Return log entries on or after `since`."""

def streak_with(itertools_walk) -> int:
    """Optional itertools-based reimplementation."""
```

Putting these in `core.py` (not in `cli.py`) means tomorrow's tests
will be easy to write — they'll test `filter_log(...)` directly without
clicking through the CLI runner. **Keep CLI files thin.** They should
parse args, call core, format output. That's it.

## Today's deliverable

- [ ] `habit reset <name>` works (with confirm or `--yes`)
- [ ] `habit recent` prints a 14-day grid
- [ ] `habit list --sort streak` sorts by longest streak first
- [ ] All tests in `tests/` pass — including the new ones for these
      features

The starter `core.py` and `cli.py` carry over from day 3 but with
TODOs for the new functions and commands. Tests for `filter_log` and
the sort key are pre-written.

## Scope check

If you're behind: skip `recent`. The grid is the most fiddly part and
the least useful. `reset` and `list --sort streak` are the high-value
two.

## Next

Tomorrow is the test-and-edge-cases day. Today's job is to make the
features *exist*. Tomorrow's job is to make them *correct*.
