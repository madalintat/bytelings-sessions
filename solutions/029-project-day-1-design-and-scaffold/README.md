---
day: 029-project-day-1-design-and-scaffold
phase: phase-1-python-core
module: phase-1-project-contacts-manager
style: story
---
# Day 29 — Project Day 1: Design and scaffold

You're starting the Phase 1 project. Open the project README first
(`../README.md`) — read the Scenario, the Requirements, and the
day-by-day plan. Today is **Day 1: design + scaffold**.

The goal of today is *not* to finish anything fancy. The goal is:

1. A `Contact` shape you can defend.
2. A `Roster` class skeleton with the indices you'll need tomorrow.
3. A working CSV loader that *normalizes on read*.
4. One subcommand that runs end-to-end: `python app.py list contacts.csv`.

That's it. By end of today you'll be able to load the sample CSV and
see a sorted list of contacts. No find, no dupes, no export — those
are tomorrow.

## Today's design choice (write it down)

Will `Roster` store **a list** or **a dict keyed by email**? Both are
valid. The README's Hint 1 picks "list + dict indices." That gives
you O(1) lookups (Day 22) without losing list order.

## What's pre-built for you

- `app.py` — a skeleton with stubbed `cmd_list`, `cmd_find`,
  `cmd_dupes`, `cmd_export`. Only `cmd_list` should work by end of
  Day 1. The others should print "(not implemented yet)" and exit 1.
- `app_test.py` — checkpoint tests for the loader and `cmd_list`.
- `data.csv` — a sample 10-row dataset with realistic mess (semicolons,
  uppercase emails, phone-number variations).

## Today's checkpoint tests

```text
$ uv run pytest app_test.py -k 'day1'
collected 4 items
test_loads_sample_csv          PASSED
test_normalizes_emails         PASSED
test_normalizes_phones         PASSED
test_list_command_runs         PASSED
```

When those pass, you're ready for Day 2.

## A small reminder

The README has graduated hints (collapsed `<details>` sections). Try
to write the loader yourself first, then peek if you're stuck for
more than ~10 minutes. Today should take 60–90 minutes.
