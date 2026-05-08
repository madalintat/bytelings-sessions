---
day: 037-async-def-await-asyncio-run
phase: phase-2-pythonic-tools
module: module-07-async-await
style: tour
---
# Day 37 — A code tour of your first `async def`

Read this whole snippet carefully. Then we'll walk it line by line.

```python
import asyncio

async def fetch_user(user_id: int) -> dict:
    print(f"  starting fetch for {user_id}")
    await asyncio.sleep(0.1)            # pretend network call
    print(f"  done fetch for {user_id}")
    return {"id": user_id, "name": f"User {user_id}"}

async def main() -> list[dict]:
    user = await fetch_user(7)
    return [user]

result = asyncio.run(main())
print(result)
```

## Line by line

`async def fetch_user(...)` — declares a **coroutine function**. Calling
it does *not* run the body. It returns a **coroutine object**, which is
basically "the body, paused at the top." This is the same pattern as a
generator function from Day 35, with extra plumbing.

`await asyncio.sleep(0.1)` — this is the magic word. `await` does two
things: it tells the event loop "I'm parked, find another task," and
it pauses the current coroutine until the awaited thing is done. You
can only use `await` inside an `async def`.

`return {"id": ...}` — a coroutine can return a value. The caller gets
it via `await`.

`async def main()` — coroutines can call other coroutines with `await`.

`result = asyncio.run(main())` — this is the **entry point** from sync
code. `asyncio.run`:

1. Creates a fresh event loop.
2. Runs the given coroutine until it returns.
3. Cleans up the loop.

You typically call `asyncio.run` exactly once, at the top of your program.
Everything beneath it is async.

## The two rules

1. **You can only `await` inside an `async def`.** A plain `def` cannot
   contain `await`. You'd get a `SyntaxError`.

2. **A coroutine that's never awaited never runs.** This is the most
   common bug you'll see this week. `fetch_user(7)` by itself is a
   *coroutine object* — inert. You must `await` it (or wrap it in a
   `Task`, see Day 38) for the body to execute. Python warns you with
   `RuntimeWarning: coroutine ... was never awaited`.

## What `await` actually does

If the awaited thing is already done, `await` returns the result
immediately — same as a sync function call. If it's not done, `await`
yields control back to the event loop, which runs other ready tasks
until the awaited thing completes.

The `async`/`await` syntax is just sugar over the iterator protocol
you saw on Day 34, plus a scheduler. You don't have to memorize the
plumbing — but if you ever need to debug it, that's the model.

## Now: open `fluency.py`

Two coroutines that look right but aren't quite.
