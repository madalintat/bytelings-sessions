---
day: 070-refactor-a-codebase
phase: phase-3-quality-production
module: module-13-refactor-in-context
style: detective
---
# Day 70 — The codebase has secrets. Find them.

The ticket says: "the duplicate-detection feature is unreliable."
You open the file. It's 200 lines. It works *sometimes*. Tests pass.
But QA can produce a wrong answer in three steps and you can't.

This isn't a bug-fix day. This is a **refactoring as investigation**
day: the act of cleaning up the code is also how you find the bug.

## The detective's mantra

When code resists understanding, it's hiding something. The hiding
spots, in order of frequency:

1. **A name that lies.** A variable called `count` actually holds a
   percentage. A function called `validate` mutates state. The lie
   isn't malicious — someone changed behavior without changing the
   name. **Renaming is investigation.** Rename to what the code
   actually does, watch the surrounding code suddenly make sense.
2. **Duplicated logic with one tiny difference.** Two near-identical
   blocks. The difference IS the bug — one of them was meant to be
   updated and got missed.
3. **Implicit state across functions.** A module-level dict that
   functions read and write. Three callers, three understandings of
   what's in it. Make the state explicit (pass it as a parameter, or
   wrap it in a class) and the inconsistency surfaces.
4. **A loop that does three things.** Iterates, validates, and
   accumulates. Pulling those apart often reveals one of them is
   wrong.

## The technique: "make the change easy, then make the easy change"

Kent Beck's line. You have a hairy function and a small bug. Don't
try to spot-fix the bug in the hairy code — you'll add another hair.
Refactor first (extract, rename, deduplicate), get the bug to *live
in one line*, then fix that line.

Concretely:

```text
1. Run the tests. Green.
2. Find the suspect region. Add a test that reproduces the bug — it goes RED.
3. Refactor (rename, extract, dedupe), keeping the OTHER tests green.
   The red test stays red — you haven't fixed it yet.
4. Once the suspect line is naked and obvious, fix it.
5. Now the red test goes green.
6. Commit each step. (`git log` becomes a story of your reasoning.)
```

## The smell-fix dictionary (cheat sheet)

| Smell | Likely fix |
|---|---|
| Function > 30 lines | Extract function (Day 68) |
| `if/elif` chain on a fixed set of values | Replace conditional with table |
| Same code in two places | Extract function or move to a helper module |
| Confusing variable name | Rename (your editor's "rename symbol" is your friend) |
| Three booleans flowing through | Replace with an enum or a state object |
| A function that returns one of three shapes | Split into three functions |
| Test that reaches deep into private internals | The class is doing too much; split it |

## Today's case

You'll be handed a small "codebase" — three functions sharing a
suspicious pattern. The bug is real. The path to it is *not* "stare
harder." The path is "rename, dedupe, then look."

## Now: open `fluency.py`

A function whose name lies. Rename it (in code AND tests) until the
name and behavior agree.
