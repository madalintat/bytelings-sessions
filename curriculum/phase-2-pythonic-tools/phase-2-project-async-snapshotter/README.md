# Phase 2 Project — Async Site Snapshotter

A 3-day build that consolidates everything from Phase 2: comprehensions
and generators, async/await with `httpx`, dataclasses and type hints,
classes and dunders, files and JSON.

## The Scenario

You're on a small platform team. Ops just stood up four new internal
services and wants a quick way to verify they're all reachable and
responding. Ad-hoc curl scripts work for one shot, but the team wants
a real tool — something that can fetch N URLs concurrently, record
status + body size + any errors, and dump the results to a JSON file
you can diff between runs.

Build that tool. Ship it in 3 days.

## Requirements

By end of Day 3 you have a CLI that:

- Reads a list of URLs from a file (one per line).
- Fetches all of them concurrently with `httpx`, capped at a
  configurable concurrency limit.
- Records each result as a `Snapshot` dataclass: `url`, `status`,
  `body_length`, `error`.
- Treats network errors (`httpx.HTTPError` family) by setting the
  `error` field. Normal HTTP status codes (including 4xx, 5xx) are
  recorded as-is — they're not errors at the network layer.
- Writes the result as JSON, indented and sort-keyed, to a path you pass
  on the command line. The write is atomic (`.tmp` + `os.replace`).
- Supports `--help` and exits cleanly on bad arguments.
- Has tests that run offline using `httpx.MockTransport`.

## Concepts checklist (Phase 2)

The project exercises:

- [x] **List/dict/set comprehensions** — building URL lists, transforming
      results, indexing failures by status code.
- [x] **Generator expressions** — feeding gathered coroutines without
      materializing intermediate lists.
- [x] **`async def` / `await`** — every fetch.
- [x] **`asyncio.gather` + bounded concurrency** — concurrent fetching
      with a `Semaphore`.
- [x] **`httpx.AsyncClient`** with `async with` — correct lifecycle,
      single client across many requests.
- [x] **Dataclasses** — `Snapshot` as a clean record type.
- [x] **`dataclasses.asdict` + JSON** — round-trip from dataclass to file.
- [x] **`pathlib.Path`** — all path arithmetic.
- [x] **Atomic writes** — temp file + `os.replace`.
- [x] **`argparse`** — the CLI surface.

## Day-by-day plan

### Day 56 — Design and scaffold

- Define the `Snapshot` dataclass.
- Stub `fetch(client, url)` and `snapshot_all(urls, fetch_fn)`.
- Build a fake-fetch CLI that walks the pipeline end-to-end with
  hard-coded data.
- Goal: the shape of the system is in place; nothing real is wired up.

### Day 57 — Build the core

- Replace the stub `fetch` with a real `httpx`-backed call.
- Convert `httpx.HTTPError` exceptions into the `error` field on the
  Snapshot.
- Add `save_snapshots(path, snapshots)` with atomic JSON output.
- Update the CLI to call the real pipeline.
- Goal: a working snapshotter you could run on a real (or mocked)
  list of URLs and get a valid JSON file out.

### Day 58 — Test and ship

- Add bounded concurrency with `asyncio.Semaphore`.
- Add a retry helper for transient failures (5xx + connect errors) but
  skip retry on 4xx.
- Polish the CLI with `argparse`: read URLs from a file, choose output
  path, choose concurrency.
- Tests: happy path, mixed errors, retry behavior, concurrency cap.
- Goal: a CLI you'd actually deploy on an internal cron.

Each day ends with a checkpoint test in `04_solo_test.py`. Get it
green before moving on.

## Hints (open only if stuck)

<details>
<summary>I'm not sure how to test async code without `pytest-asyncio`.</summary>

Define a regular `def test_x()` and call `asyncio.run(...)` inside:

```python
def test_basic():
    async def runner():
        async with _client() as c:
            return await ex.fetch(c, "http://t/ok")
    s = asyncio.run(runner())
    assert s.status == 200
```

This is what every test in this project does. No fixtures, no plugins.
</details>

<details>
<summary>How do I write a test that uses httpx without hitting the network?</summary>

`httpx.MockTransport`:

```python
def handler(request):
    return httpx.Response(200, text="ok")

client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
```

Pass that client into your code. Day 40 covered this.
</details>

<details>
<summary>asyncio.gather is sequential when I expect it to be concurrent.</summary>

You probably did:

```python
results = []
for u in urls:
    results.append(await fetch(client, u))
```

That's a sequential await loop. Use `gather`:

```python
results = await asyncio.gather(*(fetch(client, u) for u in urls))
```

Day 38 covered this.
</details>

<details>
<summary>How do I cap concurrency without breaking gather?</summary>

`asyncio.Semaphore` plus a small wrapper:

```python
sem = asyncio.Semaphore(20)

async def bounded(u):
    async with sem:
        return await fetch(client, u)

return await asyncio.gather(*(bounded(u) for u in urls))
```

Day 41 covered this.
</details>

<details>
<summary>JSON dump errors out on Snapshot.</summary>

`json.dumps` doesn't know about dataclasses. Convert first:

```python
import dataclasses
text = json.dumps([dataclasses.asdict(s) for s in snapshots], indent=2)
```
</details>

## Stretch goals

If you finish Day 58 early and want more:

1. **Throttle by host.** Per-host semaphore so you don't hammer a
   single domain even if your URL list is mostly that domain.
2. **Cache hits across runs.** Hash the URL + last-modified header,
   skip refetching if unchanged.
3. **A summary report.** Group results by status code class
   (2xx/3xx/4xx/5xx/error), print counts, pick the slowest.
4. **Real CLI tests.** Use `subprocess.run` to invoke `app.py` with
   sample input and assert on stdout.
5. **Replace `argparse` with `click`** — `click` is in the project's
   deps. See whether the cleaner decoration is worth the cost.

## Self-evaluation rubric

Before declaring the project done, check:

- [ ] You can run `uv run python day-058-.../05_apply.py urls.txt --demo`
      and it prints a one-line OK/ERR summary plus writes a valid
      JSON file.
- [ ] All four day checkpoints (`04_solo_test.py` × 3 + the working
      `app.py`) pass.
- [ ] You can explain in two sentences why bounded concurrency matters
      and how the semaphore enforces it.
- [ ] You can explain what `dataclasses.asdict` does and why it's needed
      for JSON output.
- [ ] If you change one URL's mock to raise a `ConnectError`, the JSON
      output records it with `status=0, error="ConnectError"` instead
      of crashing the whole run.
- [ ] You can name two things you'd add next if you spent a week on this.
