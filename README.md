# bytelings

**Tiny daily exercises that make code feel like a language you actually speak.**

[![PyPI](https://img.shields.io/pypi/v/bytelings.svg?color=blue)](https://pypi.org/project/bytelings/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Hey 👋

If you *kind of* know Python (or want to), but still freeze when asked to write something from scratch — this is for you. bytelings is a curriculum that meets you exactly where you are and walks you, day by day, into real fluency.

## Install

With **[uv](https://docs.astral.sh/uv/)** *(recommended — installs as a global CLI in an isolated env)*:

```bash
uv tool install bytelings
```

Or with **pip**:

```bash
pip install bytelings
```

## Get going

```bash
mkdir my-bytelings && cd my-bytelings
bytelings init     # copies the 135-day curriculum into ./curriculum/
bytelings          # starts the watcher — save a file, see green panels
```

That's it. Save a file. Watch the tests turn green. **That's the loop.**

> **What does `bytelings init` do?** It copies the bundled curriculum (135 day folders + phase projects, all the broken-on-purpose exercises and tests) into a fresh `./curriculum/` in your current directory. That's *your* working copy — you edit it, your progress saves alongside it, and `bytelings reset DAY` restores any day to its starter state. You only run `init` once, in a fresh folder.

---

## The whole idea

Most courses dump you into "implement merge sort" without first letting you *read* one, *fix* a broken one, or *fill in* a half-written one. bytelings is a ladder. You climb one rung at a time and you don't move on until your fingers know it.

Each day teaches **one concept**, and only one. You go through it like this:

**1. Read** &nbsp;—&nbsp; a short, story-styled page. Not a textbook chapter. Just enough to *feel* the idea.

**2. Drill** &nbsp;—&nbsp; a broken file with a couple of `# TODO` lines. Fix them. Tests turn green when you nail it.

**3. Guided** &nbsp;—&nbsp; here's a function signature and a docstring. You write the body.

**4. Solo** &nbsp;—&nbsp; same idea, no scaffold. Hidden tests. You write it cold, like real work.

**5. Apply** &nbsp;—&nbsp; a tiny project chunk that uses what you just wrote. The concept lands somewhere real.

The watcher (`bytelings`) runs your tests on every save and bumps you to the next rung when you pass. When you finish all 5 rungs, you wake up tomorrow on Day 2.

---

## Concept pages don't read like textbooks

Same-shape lessons make brains autopilot. So bytelings rotates across **8 different storytelling styles** — and you'll never see the same one two days in a row:

- **Story** — *"It's Monday, 9 AM. You just got hired. Here's the repo..."*
- **Pain-point** — show ugly buggy slow code first, then the fix
- **Compare two ways** — two snippets side by side, you pick the right one
- **Code tour** — read a real piece of code line by line
- **Trace** — predict what each line prints *before* you run it
- **Build it yourself** — *"Pretend Python doesn't have this. How would you build it?"*
- **Metaphor** — concepts mapped onto things from real life
- **Detective** — there's a bug, the concept is the only fix

Your brain stays alert. The fluency builds.

---

## What you'll learn — the 135-day map

| Phase | Days | What clicks for you |
|---|---|---|
| **1. Python core fluency** | 31 | Strings, lists, dicts, functions stop feeling like things you look up. |
| **2. Pythonic tools & I/O** | 27 | Comprehensions, async, dataclasses, files — you reach for the right one without thinking. |
| **3. Quality & production** | 21 | Real-world skills: pytest, logging, profiling, picking threads-vs-async-vs-processes. |
| **4. Data structures from scratch** | 19 | You build stacks, linked lists, trees, heaps, hash tables — yourself, in Python. |
| **5. Algorithms** | 25 | Recursion, sort, graphs, DP, greedy, backtracking — pattern recognition you'll use forever. |
| **6. Packaging, AST, capstone** | 12 | You ship a real CLI tool you'd actually use. |

After every phase, a **3-day project** combines everything you just learned: contacts manager → async website snapshotter → parallel log analyzer → tiny in-memory database → maze pathfinder. Phase 6 ends in an **8-day capstone** where you build, test, and ship a CLI tool of your own design.

---

## Commands

| | |
|---|---|
| `bytelings` | Start the watcher. Save → tests run → next rung. |
| `bytelings today` | What you're working on right now. |
| `bytelings progress` | Your streak and completion bar. |
| `bytelings list` | Every day with ✔ / ○ markers. |
| `bytelings hint [DAY]` | Re-read the concept page anytime. |
| `bytelings run [DAY]` | Run the current rung's tests once, no watch. |
| `bytelings reset DAY` | Start a day over. |
| `bytelings init` | Scaffold the curriculum (just once, at the start). |

---

## Why this exists

I built bytelings because I was *decent* at Python — I could read code, edit code, get things working — but I still froze when asked to write something non-trivial from scratch. I'd reach for docs. I'd google syntax. The fluency wasn't there, and no course I tried was filling that gap.

Two things were missing from every curriculum I tried:

**1. They taught topics in *blocks*** — all syntax → all data structures → all algorithms. Research keeps showing this is the worst shape for long-term retention. *Interleaved* practice — mixing topics every day — wins by a huge margin. bytelings interleaves on purpose.

**2. They skipped the bottom rungs.** They'd parachute you onto "implement merge sort" without first showing you a worked example to read, a broken version to fix, or a scaffolded version to fill in. Of course people freeze. The fix is to climb every rung.

bytelings is the curriculum I wished existed.

---

## Roadmap

The runner doesn't care what language you're learning. Each track is just curriculum content under the same `bytelings` UX.

- [x] **Python** — 135 days, shipped
- [ ] **C** — pointers, memory, the *why* behind undefined behavior
- [ ] **C++** — RAII, templates, modern C++
- [ ] **Rust** — ownership, lifetimes, fearless concurrency
- [ ] **Go** — interfaces, goroutines, the philosophy

---

## Contributing

PRs welcome — bug fixes, content polish, new languages. Adding a language is mostly: a new `bytelings/_curriculum/<lang>/` tree and a small per-language test driver. Runner core is ~1000 lines of friendly Python.

## Credits

Inspired by [Rustlings](https://github.com/rust-lang/rustlings), [Codewars](https://www.codewars.com), and [100 Days of Code](https://replit.com/learn/100-days-of-python).

## License

MIT. Fork it. Remix it. Build your own track for any language you love.

---

<sub>***The fluency comes from the reps.***</sub>
