<p align="center">
  <img src="https://raw.githubusercontent.com/madalintat/bytelings/main/assets/logo.svg" alt="bytelings" width="240" />
</p>

<h1 align="center">bytelings</h1>

<p align="center">
  <strong>Tiny daily exercises that make code feel like a language you actually speak.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/bytelings/"><img src="https://img.shields.io/pypi/v/bytelings.svg?color=blue" alt="PyPI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.12-3776AB.svg?logo=python&logoColor=white" alt="Python 3.12"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
</p>

<hr/>

Hey 👋

If you *kind of* know Python (or want to) but still freeze when asked
to write something from scratch, this is for you. bytelings is a
curriculum that meets you where you are and walks you, day by day,
into real fluency.

## Install

With **[uv](https://docs.astral.sh/uv/)** (recommended; installs as a
global CLI in an isolated env):

```bash
uv tool install bytelings
```

Or with **pip**:

```bash
pip install bytelings
```

## Get going

```bash
bytelings init           # creates ./bytelings/ with curriculum + uv project
cd bytelings
uv sync                  # installs pytest into your local .venv
bytelings                # starts the watcher; save a file, see green panels
```

That's it. Save a file. Watch the tests turn green. **That's the loop.**

> **What does `bytelings init` do?** It creates a `./bytelings/`
> project folder containing the 135-day curriculum (every day's
> broken-on-purpose exercises and tests), a ready-to-go
> `pyproject.toml` plus `uv.lock`, a `solutions/` mirror that
> `bytelings reset DAY` restores from, and a `solved/` mirror that
> `bytelings solution DAY` reveals from when you're stuck. That's
> *your* working copy. You only run `init` once.

<hr/>

## The whole idea

Most courses drop you into "implement merge sort" without first
letting you *read* one, *fix* a broken one, or *fill in* a half-written
one. bytelings is a ladder. You climb one rung at a time and you
don't move on until your fingers know it.

Each day teaches **one concept**, and only one. You go through it like
this:

**1. Read.** A short, story-styled page. Not a textbook chapter. Just
enough to *feel* the idea.

**2. Drill.** A broken file with a couple of `# TODO` lines. Fix
them. Tests turn green when you nail it.

**3. Guided.** Here's a function signature and a docstring. You write
the body.

**4. Solo.** Same idea, no scaffold. Hidden tests. You write it cold,
like real work.

**5. Apply.** A fresh problem that exercises today's concept in a new
context. Not a rerun of solo with stdin glued on.

The watcher (`bytelings`) runs your tests on every save and bumps you
to the next rung when you pass. When you finish all 5 rungs, you wake
up tomorrow on Day 2.

<hr/>

## Concept pages don't read like textbooks

Same-shape lessons make brains autopilot, so bytelings rotates across
**8 different storytelling styles** and you'll never see the same one
two days in a row:

- **Story.** *"It's Monday, 9 AM. You just got hired. Here's the
  repo..."*
- **Pain-point.** Show ugly buggy slow code first, then the fix.
- **Compare two ways.** Two snippets side by side. You pick the right
  one.
- **Code tour.** Read a real piece of code line by line.
- **Trace.** Predict what each line prints *before* you run it.
- **Build it yourself.** *"Pretend Python doesn't have this. How would
  you build it?"*
- **Metaphor.** Concepts mapped onto things from real life.
- **Detective.** There's a bug. The concept is the only fix.

Your brain stays alert. The fluency builds.

<hr/>

## When you get a test wrong, the linter teaches you

Every test ships with **per-wrong-answer diagnostic messages** in the
spirit of Kaggle's `learntools`. Get the comma wrong on Day 1 and you
see:

```
AssertionError: Your greeting is missing the comma.
The docstring shows 'Hello, <name>!' with a comma after Hello.
```

instead of a generic string diff. Every wrong answer becomes a
teaching moment, not a "spot the difference" puzzle. The mechanism is
a small `diagnose(passed, fallback_msg, *checks)` helper that any test
file in the curriculum can use.

<hr/>

## What you'll learn (the 135-day map)

| Phase | Days | What clicks for you |
|---|---|---|
| **1. Python core fluency** | 31 | Strings, lists, dicts, functions stop feeling like things you look up. |
| **2. Pythonic tools and I/O** | 27 | Comprehensions, async, dataclasses, files. You reach for the right one without thinking. |
| **3. Quality and production** | 21 | Real-world skills: pytest, logging, profiling, picking threads vs async vs processes. |
| **4. Data structures from scratch** | 19 | You build stacks, linked lists, trees, heaps, hash tables yourself, in Python. |
| **5. Algorithms** | 25 | Recursion, sort, graphs, DP, greedy, backtracking. Pattern recognition you'll use forever. |
| **6. Packaging, AST, capstone** | 12 | You ship a real CLI tool that other people install. |

After every phase, a **3-day project** combines everything you just
learned: contacts manager, then async website snapshotter, then
parallel log analyzer, then tiny in-memory database, then maze
pathfinder. Phase 6 ends in an **8-day capstone** where you build,
test, package, and *publish to PyPI* a real linter that someone other
than you can install.

<hr/>

## Recognition over recipes (the Pattern Catalog)

Programming fluency is *recognition*. bytelings ships a numbered
inventory of recurring patterns: `bytelings patterns` lists all 31,
and `bytelings patterns P-07` shows the canonical entry for any one.
Every solo and apply rung tags the patterns it exercises in a header
line:

```
"""Day 18: Build a word frequency counter.

Patterns: P-07 (accumulator-into-dict), P-12 (filter-then-map).
"""
```

Over 135 days you accumulate a vocabulary. By the time you hit graph
problems on Day 110, "this is BFS-from-source, P-26" is recognition,
not memorization.

<hr/>

## Commands

| | |
|---|---|
| `bytelings` | Start the watcher. Save, tests run, next rung. |
| `bytelings today` | What you're working on right now. |
| `bytelings progress` | Your streak and completion bar. |
| `bytelings list` | Every day with ✔ / ○ markers. |
| `bytelings hint [DAY]` | Re-read the concept page anytime. |
| `bytelings run [DAY]` | Run the current rung's tests once, no watch. |
| `bytelings start DAY` | Jump to a specific day (slug or number). |
| `bytelings reset DAY` | Start a day over (re-do its rungs). |
| `bytelings solution DAY --rung N` | Reveal a rung's canonical answer behind a friction prompt (`Y` to see, `n` to keep trying, `h` to read the hint). |
| `bytelings patterns [P-NN]` | List the Pattern Catalog or show one entry. |
| `bytelings init` | Scaffold the curriculum (just once, at the start). |

The intended path is linear (Day 1, then 2, then 3) because each day
builds on the last. If you really need to jump (cherry-picking, or
you know Day 5 cold), `bytelings start 7` will move you there. Your
streak only grows on consecutive completed days.

<hr/>

## How the watcher feels

The watcher is a single-screen TUI in the spirit of Rustlings. One
panel updates in place as you save:

```
┌──────────────────────────────────────────┐
│ day-001-uv-setup-and-pytest, Rung 2      │
├──────────────────────────────────────────┤
│ ✔ 1  Read the concept                    │
│ →  2  Fluency drill                      │
│ ○  3  Guided implement                   │
│ ○  4  Solo implement                     │
│ ○  5  Apply                              │
├──────────────────────────────────────────┤
│ ⏳ Running tests... Run #4 · 14:22:07    │
├──────────────────────────────────────────┤
│ keys: r rerun  h hint  l list  q quit    │
└──────────────────────────────────────────┘
```

Each save flips the body region through *running, then ✔ or ✘* with a
run counter so identical results still prove a fresh run happened. No
infinite scrollback of stacked panels.

<hr/>

## Why this exists

I built bytelings because I was *decent* at Python. I could read code,
edit code, get things working. But I still froze when asked to write
something non-trivial from scratch. I'd reach for docs. I'd google
syntax. The fluency wasn't there, and no course I tried was filling
that gap.

Two things were missing from every curriculum I tried:

**1. They taught topics in *blocks*.** All syntax, then all data
structures, then all algorithms. Research keeps showing this is the
worst shape for long-term retention. *Interleaved* practice (mixing
topics every day) wins by a huge margin. bytelings interleaves on
purpose.

**2. They skipped the bottom rungs.** They'd parachute you onto
"implement merge sort" without first showing you a worked example to
read, a broken version to fix, or a scaffolded version to fill in. Of
course people freeze. The fix is to climb every rung.

bytelings is the curriculum I wished existed.

<hr/>

## Roadmap

The runner doesn't care what language you're learning. Each track is
just curriculum content under the same `bytelings` UX.

- [x] **Python.** 135 days, shipped.
- [ ] **C.** Pointers, memory, the *why* behind undefined behavior.
- [ ] **C++.** RAII, templates, modern C++.
- [ ] **Rust.** Ownership, lifetimes, fearless concurrency.
- [ ] **Go.** Interfaces, goroutines, the philosophy.

<hr/>

## Contributing

PRs welcome: bug fixes, content polish, new languages. Adding a
language is mostly a new `bytelings/_curriculum/<lang>/` tree and a
small per-language test driver. Runner core is around 1000 lines of
friendly Python.

## Credits

Inspired by [Rustlings](https://github.com/rust-lang/rustlings), the
3-tier `check` / `hint` / `solution` UX from
[Kaggle's learntools](https://github.com/Kaggle/learntools), the
"four loop patterns" framing from Charles Severance's
[Python for Everybody](https://www.py4e.com/), and Andrej Karpathy's
"reinvent it before you import it" arc in
[Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero).

## License

MIT. Fork it. Remix it. Build your own track for any language you
love.

<hr/>

<sub>***The fluency comes from the reps.***</sub>
