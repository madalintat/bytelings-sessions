# bytelings

> Small daily exercises that make you fluent at writing and reading code.

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Inspired by Rustlings](https://img.shields.io/badge/inspired%20by-rustlings-orange.svg)](https://github.com/rust-lang/rustlings)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Inspired by [Rustlings](https://github.com/rust-lang/rustlings). Built
to make you reach for `dict` instead of looking it up; write a `try`
without thinking about it; recognize a sliding-window problem from one
glance. Python today — **C, C++, Rust, and Go on the roadmap.**

## Install

```bash
pip install bytelings
# or
uv pip install bytelings
```

## Quickstart

```bash
mkdir my-bytelings && cd my-bytelings
bytelings init        # copies the curriculum into ./curriculum/
bytelings welcome     # one-minute intro (optional)
bytelings             # start the watcher — save files, see green panels
```

That's it. Open `curriculum/phase-1-python-core/module-01-setup-and-values/day-001-*/`
in your editor and start fixing the broken bits.

## How it works

Each day teaches **one concept** in **5 rungs**:

1. **Read** — `concept.md`, written in one of 8 rotating storytelling
   styles (story / pain-point / compare / trace / build-it / metaphor /
   code-tour / detective). Same shape every day = autopilot. Different
   shape every day = forced re-engagement.
2. **Fluency drill** — fix a broken file. Tests turn green when you do.
3. **Guided implement** — fill a function body, signature pre-built.
4. **Solo implement** — no scaffold, hidden tests, you write it cold.
5. **Apply** — a tiny project chunk that reuses what you just wrote.

The watcher (`bytelings`) runs pytest on every save and advances you
through the rungs automatically. On rung 5 of day N, you're auto-ported
to rung 1 of day N+1.

After every 5 modules, a **3-day phase project** combines all the
phase's concepts in a real build (a contacts manager, an async website
snapshotter, a parallel log analyzer, a tiny in-memory database, a maze
pathfinder). The whole curriculum ends in an **8-day capstone** where
you ship a real CLI tool.

## Commands

| Command | What |
|---|---|
| `bytelings init` | Copy the bundled curriculum into `./curriculum/` |
| `bytelings` | Start the watcher (the main loop). Ctrl-C to exit. |
| `bytelings today` | Print what you're working on now |
| `bytelings progress` | Streak + completion bar |
| `bytelings hint [DAY]` | Show today's (or named day's) concept page |
| `bytelings run [DAY]` | Run current rung's tests once (no watch) |
| `bytelings list` | List every day with completion markers |
| `bytelings done` | Manually mark current rung done |
| `bytelings next` | Skip to next rung (escape hatch) |
| `bytelings reset DAY` | Reset a specific day's progress |
| `bytelings welcome` | Print the orientation message |

## What's in the Python track

**135 days, 6 phases, 27 modules:**

1. **Python Core Fluency** (31d) — values, strings, lists, dicts, functions, decorators, type hints
2. **Pythonic Tools & I/O** (27d) — comprehensions, async, dataclasses, classes, context managers, files
3. **Quality & Production-Grade** (21d) — errors, pytest, logging, profiling, concurrency choice
4. **Data Structures from Scratch** (19d) — stacks, linked lists, trees, heaps, hash tables
5. **Algorithms** (25d) — recursion, sorting, graphs, DP, greedy, backtracking
6. **Packaging, AST, Capstone** (12d) — `uv` packaging, AST, ship a real CLI

Phases 1–5 each end in a 3-day phase project. Phase 6 is the 8-day
capstone.

## Roadmap

- **Python** — shipped (135 days)
- **C** — planned (memory, pointers, undefined behavior intuition)
- **C++** — planned (RAII, templates, modern C++)
- **Rust** — planned (ownership, lifetimes, error handling — yes, on top of Rustlings, with a different ladder)
- **Go** — planned (interfaces, goroutines, the philosophy)

The runner is language-agnostic. Each track ships its own curriculum
and test driver under the same `bytelings` UX.

## Why this exists

Most curricula teach concepts in **blocked** order: all syntax, then
all data structures, then all algorithms. Research consistently shows
**interleaved** practice (mix topics each day) produces dramatically
better long-term retention.

And most courses skip the bottom rungs of any concept ladder — they
parachute you onto "implement merge sort from scratch" without first
giving you the worked example, the broken-file drill, or the
scaffolded version. That's why so many self-taught engineers feel
comfortable *reading* code but freeze when asked to *write* something
non-trivial.

bytelings is the curriculum I wished existed when I was decent at
Python but still reaching for syntax references daily.

## Acknowledgements

This project is **deeply inspired by**
[**Rustlings**](https://github.com/rust-lang/rustlings) (carol-nichols
& contributors). The "save → watch → green panel" loop, the `init` /
`hint` / `reset` / `run` command shape, and the "small exercises in a
single concept" philosophy all come straight from there. If you do
Rust, do Rustlings first; bytelings borrows their playbook for other
languages.

Other inspirations: [Codewars](https://www.codewars.com) and
[100 Days of Python](https://replit.com/learn/100-days-of-python).

## License

MIT. Curriculum content is also MIT — fork it, remix it, build your
own bytelings track for any language you want.

## Contributing

Bug reports, content fixes, and new-language curriculum tracks all
welcome. The runner is small (~1000 LOC); adding a new language means
shipping a new `_curriculum/<lang>/` tree and a `<lang>_test.py`
discriminator. See `CONTRIBUTING.md` (TBA).

---

*Bytes don't lie. The fluency comes from the reps.*
