---
day: day-061-pdb-and-breakpoint
phase: phase-3-quality-production
module: module-11-errors-eafp-debugging
style: detective
---
# Day 61 — A bug, a breakpoint, and a six-letter prompt

A junior engineer drops a function on your desk:

```python
def running_average(values):
    total = 0
    averages = []
    for i, v in enumerate(values):
        total += v
        averages.append(total / i)
    return averages
```

They say: "It crashes on the first element. I don't see why." You
read it. You think you see why. But you've been wrong before. Time
to **prove it**, not guess it.

## The detective's tool: `breakpoint()`

Drop one line at the top of the loop:

```python
def running_average(values):
    total = 0
    averages = []
    for i, v in enumerate(values):
        breakpoint()           # <-- the suspect's living room
        total += v
        averages.append(total / i)
    return averages
```

Run the function. Execution pauses. You get a `(Pdb)` prompt — the
six-letter prompt that means "you are now driving."

`breakpoint()` was added in Python 3.7. Before it, you wrote
`import pdb; pdb.set_trace()`. Same thing. Use `breakpoint()`.

## The six commands you actually need

| Command | What it does |
|---|---|
| `n` (next) | Run the current line, stop on the next one (don't step into calls). |
| `s` (step) | Like `n`, but step *into* function calls. |
| `c` (continue) | Run until the next breakpoint (or the end). |
| `p <expr>` | Print the value of an expression. `p i`, `p values[:3]`. |
| `l` (list) | Show the source around the current line. |
| `q` (quit) | Bail out. |

That's enough to solve almost any bug. There's also `pp` for pretty-
print, `w` for the call stack ("where am I?"), and `!<stmt>` to
execute arbitrary Python (e.g., `!total = 0` to fix state on the fly).

## Working the case

You hit the breakpoint at `i=0`. You type:

```text
(Pdb) p i
0
(Pdb) p total
0
(Pdb) n
(Pdb) p total / i
*** ZeroDivisionError: division by zero
```

Caught. The bug isn't at `total += v`. It's `total / i` when `i == 0`.
The fix is `total / (i + 1)` (or use `enumerate(values, start=1)`).

The point isn't the fix. The point is: you didn't *guess*. You
**stepped into the running program** and asked it what it knew. That
habit — questioning the code instead of theorizing about it — is the
single biggest debugging upgrade most engineers ever make.

## Now: open `02_fluency.py`

A function with a subtle bug. The test file shows the failure. Use
`breakpoint()` to find it, fix the function, then remove the
`breakpoint()` line.
