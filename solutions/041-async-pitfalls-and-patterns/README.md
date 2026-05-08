---
day: day-041-async-pitfalls-and-patterns
phase: phase-2-pythonic-tools
module: module-07-async-await
style: detective
---
# Day 41 — Three suspects in a slow async program

A teammate hands you this code. They say it's "async, but somehow not
faster than the old version." You have to find the bug. Read carefully.

```python
import asyncio, httpx, time

URLS = [f"https://api.example.com/u/{i}" for i in range(50)]

async def fetch(url):
    async with httpx.AsyncClient() as client:
        time.sleep(0.05)               # rate limit
        r = await client.get(url)
        return r.status_code

async def main():
    coros = [fetch(u) for u in URLS]
    results = []
    for c in coros:
        results.append(await c)
    return results
```

There are *three* bugs. Each one alone would tank performance. Find
them before reading on.

## Suspect 1: a fresh client per request

`async with httpx.AsyncClient()` inside `fetch` means every call
opens and closes its own connection pool. No keep-alive, no reuse,
50× the TCP handshakes. Build the client *once* in `main`, pass it in.

## Suspect 2: `time.sleep` inside async code

`time.sleep` is a **blocking** call. The whole event loop is frozen for
50 ms each time it's called. While that thread is sleeping, no other
task can run. The fix is `await asyncio.sleep(0.05)`, which parks the
current task and lets the loop run other ready tasks during the wait.

This is the most common "async didn't help" bug. Any blocking I/O —
`time.sleep`, `requests.get`, `open(...).read()`, a CPU-heavy compute
— inside an async function blocks the loop. If you need to call
blocking code from async, hand it off with `asyncio.to_thread(blocking_fn, ...)`.

## Suspect 3: awaiting in a `for` loop instead of `gather`

```python
for c in coros:
    results.append(await c)
```

This is just sequential code wearing async clothes. Each `await c`
fully completes before the next one starts. The fix is the one you saw
on Day 38: `results = await asyncio.gather(*coros)`.

## The fixed version

```python
async def fetch(client, url):
    await asyncio.sleep(0.05)
    r = await client.get(url)
    return r.status_code

async def main():
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*(fetch(client, u) for u in URLS))
```

Faster, leaner, idiomatic.

## Two more patterns worth carrying

**Bounded concurrency.** Sometimes "all 1000 at once" overwhelms the
target. A `Semaphore` caps the number running concurrently:

```python
sem = asyncio.Semaphore(20)
async def fetch(url):
    async with sem:
        return await client.get(url)
```

**Don't catch and silently swallow `CancelledError`.** A bare
`except Exception` will catch it. `CancelledError` should propagate so
parent tasks can clean up. Re-raise it explicitly if you must catch it.

## Now: open `02_fluency.py`

Two of the three suspects appear. Convict them.
