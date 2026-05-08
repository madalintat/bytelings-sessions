---
day: 075-threads-vs-async-vs-procs
phase: phase-3-quality-production
module: module-15-concurrency-in-practice
style: compare
---
# Day 75 — Threads, async, processes: pick one

Three engineers each fix the same slow service three different ways.

- Aaron uses **threads**. The code looks almost like the original.
- Bea uses **asyncio**. The code looks new — `async def`, `await`,
  `asyncio.gather`.
- Carlos uses **processes**. The code looks almost like the original
  — but it spins up workers.

All three claim victory. Two are right for this workload. One is
wrong. Which one depends on what was slow in the first place.

## Decision tree, in plain English

1. **Is the slow part CPU work in Python?** → use **processes**. The
   GIL means threads can't help; async won't either. Only processes
   spread the CPU load across cores.
2. **Is the slow part waiting on the network or disk?** → either
   **threads** or **async** works.
   - If the codebase is already sync and you're adding concurrency to
     a small slice, → **threads**. Smallest change.
   - If you're starting fresh or doing thousands of concurrent I/O
     ops, → **async**. Lower memory per task, scales further.
3. **Is the slow part the wall clock alone (`sleep`-like waits)?**
   → **async** is canonical. Threads work too.

## Side by side: 100 fake API calls

```python
# threads
from concurrent.futures import ThreadPoolExecutor
def fetch(url): return httpx.get(url).json()
with ThreadPoolExecutor(max_workers=20) as p:
    results = list(p.map(fetch, urls))
```

```python
# async
import httpx, asyncio
async def fetch(client, url):
    r = await client.get(url)
    return r.json()
async def main():
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*(fetch(client, u) for u in urls))
results = asyncio.run(main())
```

Both finish in roughly the same wall time for 100 URLs. The async
version uses ~one OS thread; the threads version uses 20. At 10,000
URLs, async wins on memory. At 100, the threads version is simpler.

## Side by side: hashing a million records

```python
# threads — DOES NOT HELP (CPU-bound, GIL)
with ThreadPoolExecutor() as p:
    list(p.map(sha256, records))
# Same wall time as the serial version, give or take.
```

```python
# processes — actually parallel
from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor() as p:
    list(p.map(sha256, records))
# Wall time / cpu_count(), roughly.
```

## The hidden costs

| Approach | Costs |
|---|---|
| Threads | Shared memory = data races; GIL = no CPU parallelism; debugging across threads is hard. |
| Async | Code style changes (`async`/`await` throughout); a single blocking call (`time.sleep`, `requests.get`) freezes everything; not all libraries are async. |
| Processes | Higher startup cost; arguments/results must `pickle`; no shared memory by default; per-process Python runtime overhead. |

The honest summary: there's no free lunch. Pick based on the
bottleneck, not the aesthetic.

## "But I want to mix them"

You can. A common pattern: an `asyncio` server that calls into a
`ProcessPoolExecutor` for CPU work via `loop.run_in_executor`. The
event loop stays responsive; the heavy lifting happens off-loop.
That's an architecture-level decision, not a daily one — keep it
simple until you have a profile that says you need it.

## Now: open `fluency.py`

A function picks the WRONG concurrency for a CPU-bound task. Switch
it from threads to processes (one-line change in
`concurrent.futures`).
