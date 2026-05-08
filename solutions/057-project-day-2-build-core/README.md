---
day: day-057-project-day-2-build-core
phase: phase-2-pythonic-tools
module: phase-2-project-async-snapshotter
style: story
---
# Day 57 — Project Day 2: build the core

You sit down on Day 2 with a working scaffold and a plan. The
`Snapshot` dataclass is solid. The fake `fetch` is producing
dummy results in input order. Today you swap the fake for a real one
and write the cache.

## Today's slice

By end of day, you should have:

- A real `fetch(client, url) -> Snapshot` that uses `httpx.AsyncClient`
  to GET each URL, captures the status code and response body length,
  and turns network errors into a Snapshot with the `error` field set.
- A `save_snapshots(path, snapshots)` function that writes the list as
  JSON, indented, atomically (Day 55 pattern).
- A working CLI that takes URLs on the command line, fetches them with
  real httpx, and writes the result to a path.

## Mental scaffolding

The pattern from Day 40 is exactly what you need:

```python
async def fetch(client, url):
    try:
        r = await client.get(url, timeout=5.0)
        return Snapshot(url=url, status=r.status_code, body_length=len(r.content))
    except httpx.HTTPError as e:
        return Snapshot(url=url, error=type(e).__name__)
```

Then in `main`:

```python
async with httpx.AsyncClient() as client:
    snapshots = await snapshot_all(urls, lambda u: fetch(client, u))
save_snapshots(out_path, snapshots)
```

`snapshot_all` from Day 56 already calls `fetch_fn(url)` and gathers
concurrently. Today you give it a `fetch_fn` that closes over a real
client.

## Why a closure?

Because `snapshot_all` doesn't know about clients — it just calls
`fetch_fn(url)`. By passing in `lambda u: fetch(client, u)`, you keep
`snapshot_all` simple and testable without httpx, while still wiring
up a real client at the call site.

## Saving as JSON

`Snapshot` is a `@dataclass`, but `json.dumps` doesn't know that. The
canonical move is `dataclasses.asdict(snapshot)` — it converts the
dataclass to a plain dict, which `json.dumps` handles natively. Map
the list and dump:

```python
import dataclasses, json
text = json.dumps([dataclasses.asdict(s) for s in snapshots], indent=2)
```

Then write atomically: write to a `.tmp` file, `os.replace` it into
place. Same pattern as Day 55.

## Testing without the network

The tests on this day use `httpx.MockTransport` (Day 40 pattern). Your
`fetch` doesn't care — it's given a client; it doesn't build one. The
test builds a client with a mock transport and passes it to `fetch`.

## What's NOT today

- Retries on transient failures.
- Concurrency caps.
- Robust CLI argument parsing.

All of those are Day 58. Today is "make the core work end to end on
the happy path plus the obvious error case."

Open `fluency.py`.
