---
day: 058-project-day-3-test-and-ship
phase: phase-2-pythonic-tools
module: phase-2-project-async-snapshotter
style: story
---
# Day 58 — Project Day 3: test, polish, ship

The core works. Day 2's CLI fetches concurrently and writes a JSON
report. Now you make it shippable. Today's three pieces:

1. **Bounded concurrency.** Without a cap, 1000 URLs at once will
   overwhelm targets, your DNS, your file descriptors, or all three.
2. **Retry transient failures.** Network blips and 5xxs deserve a
   second chance, not an immediate write of `{"error": "ConnectError"}`.
3. **Polish the CLI.** Read URLs from a file, choose the output path,
   fail fast on bad input.

## Bounded concurrency

You learned this on Day 41. A single `asyncio.Semaphore(N)` caps how
many fetches run at once.

```python
async def snapshot_all(client, urls, max_in_flight=20):
    sem = asyncio.Semaphore(max_in_flight)

    async def bounded_fetch(u):
        async with sem:
            return await fetch(client, u)

    return await asyncio.gather(*(bounded_fetch(u) for u in urls))
```

This shape is the standard one. Notice the inner closure pattern —
the semaphore is captured by reference, so all the fetches share it.

## Retries

Borrow Day 41's retry helper. Wrap `fetch` so that:
- On a `ConnectError` or 5xx response, retry up to N times with a
  short backoff.
- On a 4xx, don't retry — that's the server saying "this URL is wrong",
  not "transient failure".
- After all retries fail, return a Snapshot with the last error captured.

A common mistake: retrying on every error including 404. Don't. Only
retry **transient** failures — connection errors and 5xx codes.

## CLI polish

Three small changes turn a script into a tool:

```python
import argparse

parser = argparse.ArgumentParser(description="Fetch URLs concurrently.")
parser.add_argument("urls_file", type=Path,
                    help="File containing one URL per line")
parser.add_argument("--out", type=Path, default=Path("snapshots.json"),
                    help="Output JSON path")
parser.add_argument("--concurrency", type=int, default=20,
                    help="Max concurrent fetches")
args = parser.parse_args()

urls = [line.strip() for line in args.urls_file.read_text().splitlines()
        if line.strip()]
```

`argparse` is in the standard library and gives you `--help` for free.
Click is fancier but adds dependency overhead; for a tiny CLI like
this, argparse is the right pick.

## Tests

By Day 3, you should have tests covering:

- The happy path (2 URLs, both succeed).
- A mix of success and 4xx (4xx is recorded as-is, not retried).
- A connection error retried, then succeeding.
- A connection error retried, all attempts fail, recorded with `error`.
- The bounded concurrency: peak in-flight count never exceeds the cap.

Tests use `httpx.MockTransport` plus a small counter trick to verify
retry behavior. Today's solo lays this out.

## What you ship

A folder with `app.py` (the working CLI), `test.py` (the day's solo
checkpoint), and the three module days you climbed to get here. You
can `uv run python app.py urls.txt --out snaps.json --concurrency 50`
and it works.

This is what 27 days look like compounded.

Open `fluency.py`.
