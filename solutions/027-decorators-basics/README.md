---
day: day-027-decorators-basics
phase: phase-1-python-core
module: module-05-functions-closures-decorators
style: build-it
---
# Day 27 — Pretend `@decorator` syntax doesn't exist

You've been writing closures for two days. Today's lesson: the `@`
syntax is *just* a closure with sugar. Build it without the sugar.

## Step 1: a wrapper function by hand

You have a slow function. You want to log every call without changing
the function's body. Closures do this:

```python
def log_calls(fn):
    def wrapped(*args, **kwargs):
        print(f"calling {fn.__name__}({args}, {kwargs})")
        result = fn(*args, **kwargs)
        print(f"  -> {result!r}")
        return result
    return wrapped

def add(a, b):
    return a + b

add = log_calls(add)        # rebind `add` to the wrapped version
add(2, 3)
# calling add((2, 3), {})
#   -> 5
```

That's a decorator. The function `log_calls` takes a function and
returns a new one with extra behavior wrapped around it. The
`add = log_calls(add)` line is the part the `@` syntax replaces.

## Step 2: enter the `@`

```python
@log_calls
def add(a, b):
    return a + b
```

`@log_calls` says exactly: "after defining `add`, run
`add = log_calls(add)`." Nothing else. You can verify by reading the
generated code in the REPL — `add` is the *wrapped* function; the
original is hidden inside the closure.

## Step 3: keep the metadata

Without help, the wrapped function loses the original's name and
docstring:

```python
add.__name__       # 'wrapped'    ← lost
add.__doc__        # None          ← lost
```

`functools.wraps` fixes this:

```python
import functools

def log_calls(fn):
    @functools.wraps(fn)            # copy fn's name, docstring, etc.
    def wrapped(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result
    return wrapped
```

`@functools.wraps(fn)` copies the right attributes from `fn` onto
`wrapped`. Always include it. The day you don't, an error message
will say "wrapped" and you'll spend 10 minutes finding the file.

## A pattern you'll see hundreds of times

```python
def deco(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        # before
        result = fn(*args, **kwargs)
        # after
        return result
    return wrapped
```

The "before" can record start time, validate args, take a lock, etc.
The "after" can stop the timer, log, release the lock. The inside is
unchanged — you are inserting behavior **around** any function the
caller pins with `@deco`.

## What decorators are *good* at

- **Cross-cutting** concerns: logging, timing, retry, auth, caching.
- Things that should stay out of the function body so the body is
  just the business logic.

## What decorators are *bad* at

- Anything that depends on the function's **arguments** in a complex
  way. (You'll write decorators-with-args tomorrow for that.)
- "Two of these chained" if order matters and isn't obvious. Test it.

## Now: open `02_fluency.py`

Build a hand-rolled decorator (no `@` yet) and a `@`-style one.
