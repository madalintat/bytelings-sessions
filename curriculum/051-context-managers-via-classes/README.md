---
day: day-051-context-managers-via-classes
phase: phase-2-pythonic-tools
module: module-09-classes-dunders-context-managers
style: pain
---
# Day 51 — The 7 lines you keep forgetting to write

Look at this real code, the kind that ships and silently leaks
file descriptors:

```python
def process(path):
    f = open(path)
    data = f.read()
    result = parse(data)         # what if parse raises?
    f.close()
    return result
```

If `parse` raises, `f.close()` never runs. The file descriptor stays
open until garbage collection — eventually, but not when you wanted.
Now make this a network connection or a database transaction. The
"eventually" is now "an outage."

The fix you remember from textbooks is:

```python
def process(path):
    f = open(path)
    try:
        data = f.read()
        return parse(data)
    finally:
        f.close()
```

That's seven lines and three indentation levels for what used to be
two lines of intent. And every time you open a file, you re-type
this dance.

## The relief: `with`

```python
def process(path):
    with open(path) as f:
        return parse(f.read())
```

Two lines. The `with` block guarantees `f.close()` runs whether
`parse` succeeds, raises, or you `return` early. The cleanup is
*structural*, not something you have to remember to write.

Any object that follows the **context manager protocol** works in a
`with` block. The protocol is two methods:

- `__enter__(self)` — called on entering the block. Whatever it
  returns is bound to the `as` variable.
- `__exit__(self, exc_type, exc, tb)` — called on leaving the block,
  whether normally, by `return`, or due to an exception. The three
  args describe the exception (or are all `None` on a normal exit).

## Build one yourself

```python
class Resource:
    def __enter__(self):
        print("opening")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("closing")
        return False     # don't suppress exceptions

with Resource() as r:
    print("body")

# prints: opening / body / closing
```

The boring rules:

- `__enter__` returns the thing the user gets via `as` — usually
  `self`, sometimes a different handle.
- `__exit__` returning **truthy** suppresses the exception. Almost
  always you want `False` (or no return — `None` is falsy).
- Cleanup goes in `__exit__`. It runs even if the body raised.

## Real uses you've already seen

- `open(...)` — closes the file.
- `httpx.AsyncClient` — closes the connection pool (with `async with`).
- `lock.acquire`/`lock.release` — wrap with a `Lock` context.
- A database transaction — commit on success, rollback on exception.

Anywhere there's a "do this on entry, do that on exit" pattern, a
context manager is the right shape. You will write your own — for
test fixtures, for "change directory then change back," for "pause
the watcher, do a thing, resume."

## Now: open `fluency.py`

A class that wants to be a context manager but is missing both methods.
