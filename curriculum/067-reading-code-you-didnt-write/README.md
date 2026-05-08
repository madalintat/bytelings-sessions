---
day: day-067-reading-code-you-didnt-write
phase: phase-3-quality-production
module: module-13-reading-refactoring-style
style: tour
---
# Day 67 — A guided tour of "what does this thing do?"

It's day three at a new job. Your task is to add a feature to a 4,000-
line module someone wrote three years ago. The author left the
company. The README is two paragraphs. There are tests, sort of.

This is the most common situation in professional software. Most of
the work is *reading*, not writing. Today is the tour: a sequence of
moves that turn an unfamiliar file from intimidating to tractable.

## The five-pass read

Don't read top-to-bottom. Most code wasn't written top-to-bottom.

**Pass 1 — outline.** Skim the file. Note: imports, top-level classes
and functions, public vs `_private`. Don't read bodies. You're
sketching the *shape*. In an editor, fold every function. Three
minutes max.

**Pass 2 — entry points.** Where does control enter? Look for
`if __name__ == "__main__"`, CLI handlers, route decorators, the
public function names. Trace one path: "user does X — what's the
first line of code that runs?"

**Pass 3 — data, not code.** Find the *types* the module passes
around. Often a couple of dataclasses or dicts carry the meaning.
Once you know those, the rest of the code is just transformations
between them.

**Pass 4 — the suspect function.** Now read the bodies — but only of
the functions on the path you're changing. Skip everything else.

**Pass 5 — tests.** Read tests last. Tests document *intent*, but only
once you know the shape they're testing.

## The vocabulary you build as you read

A reader's notebook is your secret weapon. Open a scratch file. Write:

```text
ENTRY: cli.py:run() -> Pipeline.run() at pipeline.py:84
DATA:  Job (jobs.py) — id, status, payload(dict)
       Result (jobs.py) — job_id, ok, error
WHEEL: scheduler.py — picks jobs from QUEUE, fans out to workers
KEY:   Job.status transitions:  pending -> running -> done | failed
```

Five lines. You have a working mental model. You can now ask
specific questions instead of "where do I even start?"

## Tools that make reading faster

| Tool | Use |
|---|---|
| Editor's "go to definition" | Jumps to where a symbol is defined. Builds the call graph in your head. |
| `grep`/`rg` for a function name | "Who calls this?" — fan-out is what matters most. |
| `git log -p <file>` | The history of a file is its commentary. |
| `git blame` (on a confusing line) | "Why is this here?" usually has a commit message attached. |
| Run the tests | If you can read failing test names, you can read the spec. |

## The dangerous habit to avoid

The dangerous habit is **mistaking reading effort for understanding**.
You stare at a function for ten minutes; you feel like you must
understand it; you don't. The cure is concrete: after you read a
function, *say what it does in one English sentence, out loud*. If
you can't, you don't yet understand it. Drop a `breakpoint()` and run.

Tomorrow you'll *change* code. Today you build the read-it-first habit
that separates engineers who can drop into any codebase from those
who can only work where they wrote the original.

## Now: open `02_fluency.py`

A small, mildly-confusing function. Annotate it with a one-line
docstring that describes what it does. Tests check your docstring.
