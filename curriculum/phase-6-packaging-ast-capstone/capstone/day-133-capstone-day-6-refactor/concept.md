---
day: day-133-capstone-day-6-refactor
phase: phase-6-packaging-ast-capstone
module: capstone
style: pain
---
# Capstone Day 6 — Refactor (with the safety net)

You have working code. You have tests. Today you make the working
code *good*. The tests stop you from making it bad.

## What "refactor" means here

Not "rewrite." Not "add features." Refactor:

> Restructure code without changing what it does.

The test suite is your contract. Before refactor: green. After
refactor: green. The diff in between can look as wild as you want.

If you're nervous about a change, run the tests first. If a refactor
breaks tests *and* the new code looks better, the test was checking
the wrong thing — fix the test. If the new code looks worse, undo.

## The pain points to look for

Read your own code with fresh eyes. Hunt for these:

### 1. The same shape, twice

You wrote `mark_done` and `streak` and they both build `set(self.log)`
internally? That's fine. But if you have *three* places building the
same set, extract `_logged_dates(self) -> set[date]`. Keep it private
(`_` prefix).

### 2. Long function

Anything over 30 lines is suspect. Anything with more than two levels
of nesting is suspect. The fix is usually to extract a helper.

### 3. Vague names

`def process(habit, today)` tells you nothing. `def streak(habit,
today)` tells you everything. Rename until each function name pays
for itself.

### 4. The "what does this comment mean" comment

```python
# Hack: have to add 1 because of midnight thing
n += 1
```

That comment is a tombstone for a reasoning chain that wasn't
captured. Either:
- Replace the magic +1 with a `if today_is_first_log_day(...)` branch
  whose name explains itself, OR
- Expand the comment into a proper docstring or `RFC`-style note.

### 5. A class that's a dict

If your `Habit` dataclass is *only* used as a glorified dict — passed
around, fields read, never any methods called — collapse it. Conversely,
if you pass a dict everywhere and `dict["log"]` typos haunt you, promote
it to a dataclass.

### 6. An import you need to fix

`from .core import *` is forbidden. List the names. Future you will thank
present you.

## A specific refactor I'd encourage

In `cli.py`, there's likely a chunk like:

```python
path = storage.default_data_path()
habits = storage.load(path)
# ... do work ...
storage.save(path, habits)
```

This shape repeats. Extract a context manager:

```python
from contextlib import contextmanager

@contextmanager
def open_db():
    path = storage.default_data_path()
    habits = storage.load(path)
    try:
        yield habits
    finally:
        storage.save(path, habits)
```

Now every command reads:

```python
with open_db() as habits:
    storage.mark_done(habits, name, date.today())
```

This is exactly what Module 9 (context managers) was preparing you
for. The pattern shows up in every database client, every transaction
manager, every "load, mutate, save" sequence in real software.

## Concepts you're using

- **Context managers (M9)** — `@contextmanager` for `open_db`.
- **Refactoring patterns (M13)** — extract function, extract method,
  rename, replace dict with dataclass.
- **Reading code (M13)** — your own code, with a critical eye.
- **Testing as safety net (M12)** — green-refactor-green is the loop.

## Today's deliverable

- [ ] At least 3 refactors landed
- [ ] Tests still green after each one
- [ ] At least one extracted helper function
- [ ] At least one place where you used a context manager

The starter has the day 5 code wholesale. Edit it freely.

## Honest moment

If on day 6 you discover a real design flaw — `mark_done` should have
been `record(date)`, the JSON shape is awkward — and fixing it means
breaking tests, fix it. Better to know on day 6 than next month.

## Next

Tomorrow: polish. Logging, error messages, `--verbose`, `--quiet`. The
production-ready stuff.
