---
day: 072-profiling-with-cprofile
phase: phase-3-quality-production
module: module-14-logging-profiling-perf
style: tour
---
# Day 72 — A guided tour of cProfile

The job is slow. It used to take 5 seconds. Now it takes 50. Your
team has theories. ("Probably the JSON parsing." "I bet it's the
regex.") **Theories are noise. Profilers are signal.**

`cProfile` is Python's built-in deterministic profiler — it ships in
the standard library, costs about 2x runtime when active, and tells
you exactly which function ate the wall clock. Today is the tour.

## Three ways to invoke it

### From the command line

```text
$ python -m cProfile -s cumulative -o out.prof your_script.py
$ python -m pstats out.prof
% sort cumulative
% stats 15
```

This dumps stats to `out.prof` (which `pstats` reads), sorted by
**cumulative time** (we'll get to which sort to use). The `pstats`
shell shows the top 15.

### Around a block of code

```python
import cProfile, pstats

with cProfile.Profile() as pr:
    do_the_thing()

pstats.Stats(pr).sort_stats("cumulative").print_stats(15)
```

This is what you'll use in scripts and tests. The `with` block scopes
exactly what you're profiling — no surrounding setup pollutes the
results.

### Around a function (decorator pattern)

You'll often write a tiny helper:

```python
def profiled(fn):
    def wrapper(*a, **kw):
        with cProfile.Profile() as pr:
            result = fn(*a, **kw)
        pstats.Stats(pr).sort_stats("cumulative").print_stats(15)
        return result
    return wrapper
```

Drop `@profiled` on the slow function during investigation. Remove
it before merging.

## Reading the output

You'll see columns like:

```text
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.501    0.001    1.234    0.001 parser.py:42(parse)
    20000    0.300    0.000    0.300    0.000 {method 'split' of 'str'}
```

- `ncalls` — how many times the function ran.
- `tottime` — time spent IN the function, *excluding* time in callees.
- `cumtime` — time spent in the function INCLUDING callees.

**The two sorts you actually use:**

- `sort_stats("cumulative")` (cumtime) — answers "where is the
  program spending its wall clock?" Top entry is usually `main`/
  `<module>`. Walk down until you find a function you didn't expect
  near the top.
- `sort_stats("tottime")` (tottime) — answers "which leaf function
  is doing the work?" Useful for finding the hot inner loop.

Use cumulative first to find the slow *path*. Switch to tottime to
find the slow *line on that path*.

## What cProfile won't tell you

- **Wall clock vs CPU.** cProfile measures CPU + I/O wait equally;
  if your bottleneck is "waiting on the network," cProfile correctly
  shows that, but it can't accelerate it.
- **Memory.** For memory profiling, you want `tracemalloc` (in the
  stdlib) or `memray` (third-party).
- **Async.** cProfile works with `asyncio`, but the call graph
  through `await`s is harder to read. Tomorrow's day uses concrete,
  CPU-bound examples.

## A tiny mental model

> The slow thing is almost never where you think.

That's the whole reason we profile instead of guess. Profile, *then*
optimize the function the data points to — not the one your gut
points to. You will be surprised. Embrace the surprise.

## Now: open `fluency.py`

A profiler decorator skeleton. Make it return the result and print
stats sorted by cumulative time.
