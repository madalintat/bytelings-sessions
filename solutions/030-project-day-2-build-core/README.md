---
day: day-030-project-day-2-build-core
phase: phase-1-python-core
module: phase-1-project-contacts-manager
style: story
---
# Day 30 — Project Day 2: Build the core

Yesterday you scaffolded. Today you fill in the meat.

By end of today, all four commands work end-to-end:

```text
$ uv run python app.py list   data.csv
$ uv run python app.py find   data.csv --email alice@example.com
$ uv run python app.py find   data.csv --regex "^Bob"
$ uv run python app.py dupes  data.csv
$ uv run python app.py export data.csv /tmp/clean.csv
```

## What's pre-built

- The Day 1 `app.py` is here, with the same `load_csv`, `Roster`,
  `cmd_list`, and CLI plumbing.
- `cmd_find`, `cmd_dupes`, `cmd_export` still print "(not
  implemented)" — those are today's work.
- A `@timed` decorator stub is included; you'll wrap `cmd_find` and
  `cmd_dupes` with it.
- `app_test.py` includes Day 2 checkpoint tests.

## Today's design choices

1. **Find by email/phone**: O(1) via the `by_email` / `by_phone`
   indices the `Roster` already carries. No loops.
2. **Find by regex**: O(n) — must scan. The regex matches against the
   name only (per the README spec).
3. **Dupes**: build a `defaultdict(list)` keyed by
   `(name_initials, phone_digits)`. One pass. Skip groups of size 1.
4. **Export**: write a clean CSV. Comma separator. Always 3 columns.

## The `@timed` decorator

Two layers, with `functools.wraps`. It prints elapsed milliseconds to
stderr after each call. Don't print to stdout — that pollutes the
search output.

## Today's checkpoint tests

```text
$ uv run pytest app_test.py -k 'day2'
test_find_by_email          PASSED
test_find_by_regex          PASSED
test_dupes_finds_clusters   PASSED
test_export_round_trip      PASSED
test_timed_prints_to_stderr PASSED
```

If those pass, you're ready for Day 3 (testing + ship).

## A reuse hint

You wrote `english_list` (Day 8), `dedupe` (Day 15), and various
decorator patterns (Days 27–28). You'll find places to reuse those
patterns here — or not. The point is to *see* the opportunities.
