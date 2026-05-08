---
day: 039-async-iterators-and-async-for
phase: phase-2-pythonic-tools
module: module-07-async-await
style: trace
---
# Day 39 — Trace this: when does the async generator yield?

Predict the order of every print *before* you run it.

```python
import asyncio

async def ticks():
    print("A: enter ticks")
    yield 1
    await asyncio.sleep(0.0)
    print("B: after first yield")
    yield 2
    print("C: after second yield")

async def main():
    print("--make agen--")
    agen = ticks()
    print("--first async for--")
    async for v in agen:
        print(f"got {v}")
    print("--done--")

asyncio.run(main())
```

The output:

```text
--make agen--
--first async for--
A: enter ticks
got 1
B: after first yield
got 2
C: after second yield
--done--
```

Calling `ticks()` doesn't run the body — exactly like a regular
generator. The `async for` is what drives it. Each iteration calls the
generator's `__anext__()`, which is itself a coroutine — that's why
you can `await` inside the body.

## What you've got here

- A function defined with `async def` *and* containing `yield` is an
  **async generator function**. Calling it returns an async generator.
- `async for x in agen:` is the async cousin of `for x in gen:`. It
  awaits each `__anext__` to get the next value.
- The body of an async generator can contain both `yield` (produce a
  value) and `await` (pause for I/O).

## Why this exists

Imagine streaming results from a paginated API. Each page is a network
call. You don't want to load all pages into memory before the caller
sees anything. You want:

```python
async for record in stream_records():
    process(record)
```

That's exactly what async generators give you. The `async def` lets
the body await fetches; the `yield` lets the caller iterate one
record at a time.

## The async iterator protocol

If you want to write your own (instead of using `async def` + `yield`),
implement two methods:

```python
class Pager:
    def __aiter__(self):
        return self
    async def __anext__(self):
        if no_more:
            raise StopAsyncIteration
        return await fetch_one_page()
```

Note: `StopAsyncIteration`, not `StopIteration`. Different sentinel.

## Comprehensions, async edition

You can write async-flavored comprehensions:

```python
results = [x async for x in stream()]
```

This is shorthand for an `async for` loop that builds a list.

## Now: open `fluency.py`

A broken async generator + a usage site that uses the wrong loop.
