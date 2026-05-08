---
day: day-074-the-gil-and-concurrent-futures
phase: phase-3-quality-production
module: module-15-concurrency-in-practice
style: tour
---
# Day 74 — A guided tour of the GIL and `concurrent.futures`

You have a script that does ten HTTP requests, sequentially, and
takes ten seconds. You think: "threads will fix this." You also have
a script that crunches a billion floats, and you think the same
thing. One of those guesses will work. The other will *make things
worse*. Today: why.

## The Global Interpreter Lock, in one paragraph

CPython runs only one thread of *Python bytecode* at a time. There's
a lock — the GIL — held by whichever thread is currently running
Python. When that thread does I/O (`socket.recv`, `file.read`,
`time.sleep`), it releases the GIL so other threads can run. When it
does pure CPU work in Python, the GIL stays held until the OS
preempts it (every few ms).

So:

- **I/O-bound work** (waiting on network, disk, sleep) → threads help.
  Multiple requests in flight; the GIL is released during the waits.
- **CPU-bound work** (number crunching in Python) → threads don't
  help. They just shuffle the lock between cores; total work is the
  same. Use **processes** instead (next two days).

Note: Python 3.13 added an optional **free-threaded** build that
removes the GIL. Most code today still runs on the standard build,
which has the GIL. Plan for it.

## `concurrent.futures` — the unified API

The standard library gives you two pools with the same shape:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
```

Same methods: `.submit(fn, *args)`, `.map(fn, iterable)`, `.shutdown()`.
Same return types: `Future` objects. The pool you pick is the
question; the API is the same.

## The two patterns you'll use weekly

### Pattern 1: `map` for "run this on every item"

```python
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    return httpx.get(url).status_code

urls = ["https://...1", "https://...2", "https://...3"]

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(fetch, urls))
```

`pool.map` returns results in input order, just like `map`. The
`with` block waits for everything to finish before exiting.

### Pattern 2: `submit` + `as_completed` for "fire and react as they finish"

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=8) as pool:
    futures = {pool.submit(fetch, u): u for u in urls}
    for fut in as_completed(futures):
        url = futures[fut]
        print(url, fut.result())
```

`as_completed` yields futures *in finish order*, so you can stream
results, log progress, or short-circuit on first success.

## Picking `max_workers`

Rule of thumb:

| Work type | Pool | `max_workers` |
|---|---|---|
| Network I/O | `ThreadPoolExecutor` | 8–32 (it's I/O wait, not CPU) |
| Disk I/O | `ThreadPoolExecutor` | 4–8 |
| Pure CPU | `ProcessPoolExecutor` | `os.cpu_count()` |

Going too high on threads doesn't help (GIL contention) and may
hurt (memory, context switches).

## Errors and surprises

A future's `.result()` re-raises the function's exception in the
caller. So if `fetch(url_3)` raised, `pool.map(...)` will re-raise
when you iterate to that result, *not* during `.submit`. Wrap
`fut.result()` in `try/except` if you want to log-and-continue.

`pool.map` has a `timeout` argument; `submit().result()` accepts one
too. Use them in production paths so a stuck call doesn't wedge the
pool.

## Now: open `02_fluency.py`

Convert a sequential `for`-loop of "fake API calls" to a thread pool.
