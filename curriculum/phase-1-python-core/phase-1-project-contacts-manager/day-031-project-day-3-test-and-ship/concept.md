---
day: day-031-project-day-3-test-and-ship
phase: phase-1-python-core
module: phase-1-project-contacts-manager
style: story
---
# Day 31 — Project Day 3: Test and ship

You have a working tool. Today: harden it, test it, polish it, and
mark Phase 1 done.

## Three jobs today

### 1. A real test suite

`app_test.py` already has the Day 1 + Day 2 checkpoints. Today, **add at
least 4 more tests** under `# day3` markers. Cover at least:

- An empty CSV (header only) loads to an empty roster.
- A malformed line (wrong number of fields) is skipped silently.
- `find --regex` with a pattern that matches nothing returns exit code 1.
- A round-trip: `export` then `load` produces the same data.

### 2. Error handling

The tool should never crash with a tracebacked Python error on
"normal" bad input. For each of these, return a nonzero exit code
with a friendly stderr message:

- File doesn't exist (Day 1 already did this).
- File is unreadable (permission denied).
- Find called with no flag.
- Export called with no out path.

### 3. Polish

- A 1-line banner at the top of `--help` describing the tool.
- Sort dupes output deterministically (by group's first contact's name).
- Print the file's contact count after `list` to stderr (so it stays
  out of pipes).

## A note on shipping

"Shipping" here means: you ran `uv run pytest app_test.py` and it's all
green; you ran `uv run python app.py list data.csv` and it does what
the README promises; the rubric in `../README.md` has all six boxes
checked.

You're not packaging this yet. Real packaging waits for Phase 6
(Module 25). For now: a single Python file, a test, a CSV, a sample
run.

## Phase 1: done

Phase 1 was 31 days. You've practiced:

- A working dev environment (uv + pytest)
- Numbers, booleans, identity, type hints
- Strings down to bytes, parsing, regex
- Lists, dicts, sets, hashing
- Big-O intuition
- Functions, closures, decorators with args
- And one real CLI tool that ties it all together

Phase 2 (Pythonic Tools & I/O) starts next: comprehensions,
generators, async, dataclasses, dunders, files. Most of what we'll
build on top of Phase 1 is *style* — making correct code Pythonic.

Take a beat. Then `uv run swe today` to start Day 32.
