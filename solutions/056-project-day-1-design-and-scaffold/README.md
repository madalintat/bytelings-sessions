---
day: 056-project-day-1-design-and-scaffold
phase: phase-2-pythonic-tools
module: phase-2-project-async-snapshotter
style: story
---
# Day 56 — Project Day 1: design and scaffold

You wrap up Module 10 on a Friday. Monday morning, your team lead drops
a ticket on you:

> "We need a CLI that fetches a list of URLs concurrently, parses the
> response into typed records, and caches the result as JSON. Make it
> reusable. Three days."

You smile a little. You've spent the last 24 days learning the exact
pieces this needs: comprehensions, generators, async/await with httpx,
dataclasses, context managers, pathlib, JSON. Today is design day.

## What you're building

A small library + CLI called **`snapshotter`**. Given a list of URLs,
it:

1. Fetches all of them concurrently with `httpx`.
2. Records each result as a `Snapshot` dataclass.
3. Writes the result as JSON to a path you pick.
4. Skips URLs that fail and reports them.

The full requirements live in the project README. Today, the goal is
narrower: pick the shape of your code, write the dataclass, and stub
the entry points.

## Today's slice

By end of day, you should have:

- A `Snapshot` dataclass with the fields the project will produce.
- A function `fetch(client, url) -> Snapshot` (async). For now, it
  can be a stub that returns a dummy snapshot.
- A function `snapshot_all(urls) -> list[Snapshot]` (async). Stub it
  to call `fetch` for each URL and return a list.
- The 5 rungs of this folder walk you through getting there.

You'll wire up the real concurrency and the file I/O on Day 57.
You'll add tests, error handling, and CLI polish on Day 58.

## Why "looser" than a Ladder Day

Ladder Days are tightly scoped: one concept, one drill, one solo. A
Project Day stitches three or four concepts into a tiny working chunk.
Tests are still here — they describe what the slice should *do* — but
they're more end-to-end. Don't be surprised if rung 4's solo tests
pass only after you've wired up the function `app.py` actually calls.

## The plan

- **Day 1 (today):** dataclass + stubs + CLI argument parsing.
- **Day 2:** real httpx fetch + concurrency + JSON output.
- **Day 3:** error handling + retry + tests + polish.

Open the README at the project root if you haven't yet. Then come back
here and start with `fluency.py`.
