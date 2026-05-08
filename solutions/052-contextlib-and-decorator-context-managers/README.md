---
day: 052-contextlib-and-decorator-context-managers
phase: phase-2-pythonic-tools
module: module-09-classes-dunders-context-managers
style: tour
---
# Day 52 — A code tour of `contextlib`

Yesterday you wrote context managers as classes. That's the long form.
The short form is one decorator.

```python
from contextlib import contextmanager

@contextmanager
def cd(path):
    import os
    old = os.getcwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(old)
```

Read it like a function with a single `yield`. Everything before
`yield` is `__enter__`. The yielded value is what `as` binds to.
Everything after `yield` is `__exit__`. The `try/finally` is what
makes cleanup run even if the body raises.

Usage:

```python
with cd("/tmp") as p:
    print(p)        # /tmp
# back to the original directory
```

That's the whole tour, but `contextlib` has more pieces worth knowing.

## `closing(thing)` — auto-close anything with `.close()`

Some libraries give you objects that have a `.close()` method but
aren't context managers. `closing` wraps them:

```python
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen(url)) as page:
    data = page.read()
```

On exit, `closing` calls `page.close()`. One line. No try/finally.

## `suppress(*excs)` — built-in version of yesterday's `Suppress`

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("maybe-missing.tmp")
```

Same idea as your hand-rolled `Suppress`, but in the standard library.

## `ExitStack` — when N is unknown until runtime

You have a list of files to open. You don't know N at write time.
Nesting `with` blocks doesn't generalize. `ExitStack` does:

```python
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in paths]
    # use files... all of them get closed on exit
```

`enter_context` registers the object's `__exit__` to run when the
stack exits. Whatever order they entered, they exit in reverse.

## `@contextmanager` rules of thumb

- Exactly one `yield`. More than one and you'll get a confusing
  RuntimeError.
- Wrap the `yield` in `try/finally` so cleanup runs on exception.
- If you want to *suppress* an exception inside the body, catch it
  around the yield. The `@contextmanager` form handles that — the
  body's exception is re-raised at the `yield` site.

## Pick the form

- **Class-based** (`__enter__`/`__exit__`): when the object has
  state and methods you want to call inside the block.
  (`with httpx.AsyncClient() as client: client.get(...)`.)
- **`@contextmanager` function**: when it's just "do X, then do Y at
  the end." Logging timers, temp directories, monkeypatched env vars.
- **`closing` / `suppress` / `ExitStack`**: when your problem already
  matches one of contextlib's recipes.

## Now: open `fluency.py`

A class-form context manager rewritten as a function with a missing
piece — wire it up.
