---
day: day-128-capstone-day-1-pick-and-design
phase: phase-6-packaging-ast-capstone
module: capstone
style: story
---
# Capstone Day 1 — Pick what you're building

You've finished 127 days. The next 8 are different. There are no
ladder rungs. No hidden tests waiting. Just: build one real thing,
end-to-end, and ship it.

Today is the design day. **Tomorrow you start scaffolding.** The goal
of today is to have a one-page design doc and a project name that
makes you a little proud to type.

## The recommended project: `habit`

A small command-line tool for tracking daily habits. Type
`habit done meditate` and it records you did it today. Type
`habit list` and it shows your current streaks. Data lives in a
single JSON file in `~/.config/habit/data.json`.

It's small. It's useful. You'll actually use it. And it touches every
phase of the curriculum:

| Phase | Concepts you'll exercise |
|---|---|
| 1 (core) | strings, lists, dicts, functions, type hints |
| 2 (tools/IO) | dataclasses, files, JSON, context managers |
| 3 (quality) | errors, EAFP, pytest, logging |
| 4 (data structures) | dict-as-index, deque for recent-events log (optional) |
| 5 (algorithms) | streak calc is a tiny consecutive-days problem |
| 6 (this phase) | pyproject, console scripts, maybe a tiny lint rule |

## Or substitute your own

You'll spend 8 days on this. If you have a better idea — something
*you* will actually use — pick that. Good capstone candidates:

- **`toc`** — read a markdown file, print a table of contents from the
  headings.
- **`linkcheck`** — async crawl one site and report broken links.
- **`logslice`** — given a log file and a time window, extract the
  matching lines and summarize errors.
- **`ssg`** — a 200-line static site generator that turns a folder of
  markdown into a folder of HTML.
- **`pkginfo`** — given a `pyproject.toml`, print a dependency report
  (the rung 5 from day 124, made real).

Pick something with the same shape as `habit`: one CLI, one local data
format, two or three subcommands, no networking required for v1.

## Today's deliverable

Write a one-page design in `design.md` (in this day folder). It must
answer five questions:

1. **What does it do?** One paragraph, plain English.
2. **What are the commands?** List subcommands and their args.
   `habit done <name>`, `habit list`, `habit reset <name>`.
3. **What's the data shape?** Sketch the JSON. Don't engineer it —
   just write something plausible.
4. **What can go wrong?** List the 3-5 things that will need error
   handling. (Missing config dir? Corrupt JSON? Habit name with spaces?)
5. **What's out of scope for v1?** This is the most important
   question. Write down what you *won't* do. Sync? Charts? Reminders?
   Multi-user? Cross those off now.

There's a `design.md` template in this folder. Open it, fill it in,
commit it. Tomorrow you write the `pyproject.toml`.

## A note on scope

8 days feels like a lot. It isn't. You'll spend day 132 on tests, day
134 on polish, day 135 on packaging. The actual *building* is days
129-131 — three days. Plan for that.

If on day 132 the thing isn't done: **cut features, don't extend
days**. A shipped tool with three commands beats an unshipped tool
with seven.

## Next

Open `design.md`, fill it in. Then peek at `notes.py` to play with the
data shape in a REPL. There's no test to make pass today — but
there's also nothing stopping you from running `uv run pytest` here:
the tiny `test_design.py` will just confirm your `design.md` exists
and isn't empty.
