---
day: 040-real-world-async-with-httpx
phase: phase-2-pythonic-tools
module: module-07-async-await
style: story
---
# Day 40 — The status page

It's 4:50 PM on a Friday. Your team owns three internal services. Ops
just added a fourth. Someone slacks the channel:

> "Quick — can we get a one-page health check that pings all four
> services and shows green/red? It needs to be fast."

You open a fresh file. You know two things:

1. Each ping is a tiny HTTP GET. They have nothing to do with each
   other. Doing them sequentially is silly.
2. You've used `requests` before. You vaguely remember `requests` is
   sync and there's a thing called `httpx` that's async.

You install nothing — `httpx` is already in the project's deps. You
write this:

```python
import asyncio, httpx

URLS = [
    "https://api.example.com/auth/health",
    "https://api.example.com/billing/health",
    "https://api.example.com/notify/health",
    "https://api.example.com/search/health",
]

async def check(client, url):
    r = await client.get(url, timeout=2.0)
    return url, r.status_code

async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*(check(client, u) for u in URLS))
    for url, code in results:
        mark = "OK" if code == 200 else f"FAIL ({code})"
        print(f"{mark:<10} {url}")

asyncio.run(main())
```

Total run time on your laptop: ~250 ms. Sequential, it would have been
~1 second. The PM is happy. You go home.

## What you used

- **`httpx.AsyncClient`** — the async cousin of `httpx.Client`. Its
  methods (`get`, `post`, etc.) are coroutines, so you `await` them.
- **`async with`** — context-manager flavor of `with`. The client opens
  a connection pool on entry and closes it on exit. Always use it; a
  leaked client is a leaked socket.
- **One client, many requests.** You build the client once and pass it
  around. You do NOT `httpx.AsyncClient()` per request — that defeats
  connection pooling and is much slower.
- **`asyncio.gather`** — fires off all four `check` coroutines, awaits
  the lot, returns results in input order.

## The shape, generalized

```python
async with httpx.AsyncClient(timeout=10.0) as client:
    results = await asyncio.gather(*(work(client, x) for x in inputs))
```

That single shape covers most "fan out N HTTP calls, wait for all"
problems you'll ever write. It also generalizes to "fan out, then
process each result" — just chain another async pipeline after gather.

## Tests without the network

Real HTTP calls in tests are flaky and slow. `httpx.MockTransport` lets
you build a client that responds from a Python function instead of a
network. Your code doesn't change — only the client setup does:

```python
def handler(request):
    return httpx.Response(200, text="pong")

transport = httpx.MockTransport(handler)
async with httpx.AsyncClient(transport=transport) as client:
    ...
```

Tomorrow's tests use this pattern.

## Now: open `fluency.py`

A status checker that's almost right but uses the wrong client.
