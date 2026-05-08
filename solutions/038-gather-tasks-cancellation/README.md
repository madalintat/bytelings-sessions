---
day: day-038-gather-tasks-cancellation
phase: phase-2-pythonic-tools
module: module-07-async-await
style: pain
---
# Day 38 — When async is just as slow as sync

You wrote your first async code yesterday. You're proud. Then you ship
this:

```python
async def fetch_all(ids):
    results = []
    for i in ids:
        results.append(await fetch_one(i))
    return results
```

And you time it:

```text
fetched 10 items in 1.02s
```

Each `fetch_one` takes 100ms. Ten of them. Sequential. You wrote async
and got nothing.

## Why this is sequential

The `for` loop awaits one fetch fully before starting the next one.
The event loop is happy to run other tasks during the wait — but you
didn't *give it* other tasks. There's exactly one chicken in one oven
at a time.

## The fix: `asyncio.gather`

```python
async def fetch_all(ids):
    return await asyncio.gather(*(fetch_one(i) for i in ids))
```

`gather` takes a bunch of coroutines, schedules them all on the loop
at once, awaits them all, and gives you back a list of results in the
*same order* as the inputs. Now ten fetches overlap; total time drops
to ~100ms.

```text
fetched 10 items in 0.11s
```

That's the win.

## Tasks: when you need to start a coroutine without awaiting yet

`asyncio.create_task(coro)` schedules a coroutine on the loop and
returns a `Task` object. The task runs in the background. You can do
other work, then `await task` later to get the result.

```python
task = asyncio.create_task(fetch_one(7))
# ... do something else ...
result = await task
```

This is what `gather` is doing under the hood.

## Cancellation

A task can be cancelled. `task.cancel()` schedules a `CancelledError`
to be raised inside the task at its next `await` point. The task
should typically let the exception propagate — that's how cleanup
runs.

```python
task = asyncio.create_task(slow_thing())
await asyncio.sleep(0.1)
task.cancel()
try:
    await task
except asyncio.CancelledError:
    print("cleaned up")
```

Pattern: launch tasks, race them with timeout or some signal, cancel
the losers. `asyncio.wait_for(coro, timeout)` does exactly this — it
runs the coroutine, and if it doesn't finish in `timeout` seconds, it
cancels it and raises `TimeoutError`.

## Now: open `fluency.py`

A sequential fetch loop that needs to become a `gather`.
