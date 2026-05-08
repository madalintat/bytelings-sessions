---
day: day-028-decorators-with-args-and-type-hints
phase: phase-1-python-core
module: module-05-functions-closures-decorators
style: tour
---
# Day 28 — Tour: a decorator that takes arguments

Yesterday's `@retry` always retried 3 times. What if the caller wants
5? You need a decorator with **arguments**:

```python
@retry(times=5)
def fetch():
    ...
```

Read this snippet. The trick is hiding in plain sight.

```python
import functools
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def retry(*, times: int = 3, on: type[Exception] = Exception) -> Callable:
    """Retry the wrapped function up to `times` total attempts."""
    if times < 1:
        raise ValueError("times must be >= 1")

    def decorator(fn: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(fn)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exc: BaseException | None = None
            for _ in range(times):
                try:
                    return fn(*args, **kwargs)
                except on as e:
                    last_exc = e
            assert last_exc is not None
            raise last_exc
        return wrapped
    return decorator
```

A line-by-line tour:

1. **`def retry(...) -> Callable:`** — `retry` is now a function that
   *returns a decorator*. So `@retry(times=5)` is calling `retry(...)`,
   which returns a decorator, which then decorates `fetch`.
2. **`*, times: int = 3, on: type[Exception] = Exception`** —
   keyword-only args; `on` is the exception class to catch (default
   "any exception"). Both have defaults so `@retry()` works too.
3. **`if times < 1: raise`** — fail fast on bad config. The error
   surfaces at *decoration time*, not when the function runs.
4. **`def decorator(fn): ... return wrapped`** — the inner shape is
   exactly yesterday's decorator. The outer wrapper is the new layer.
5. **`@functools.wraps(fn)`** — copy fn's metadata onto `wrapped`.
6. **`P = ParamSpec("P"); R = TypeVar("R")`** — type-hint shapes.
   `ParamSpec` says "whatever args/kwargs `fn` takes." `TypeVar`
   says "whatever return type `fn` has." Together they tell the type
   checker that `wrapped` has the *same* signature as `fn`.
7. **`Callable[P, R]`** — "a callable that takes parameters of shape
   P and returns R." The hint preserves the underlying function's
   signature through the wrapper, so editors and mypy don't lose it.

## The two-vs-three-layer rule

| You write | Layers |
|---|---|
| `@deco` (no parens) | `def deco(fn) → wrapped` (2 layers) |
| `@deco()` or `@deco(arg=val)` | `def deco(arg) → def real_deco(fn) → wrapped` (3 layers) |

It's the same idea: the `@` consumes whatever expression follows it,
and that expression must evaluate to something that takes `fn` and
returns `wrapped`. With arguments, you call `deco(...)` first, and
*that call's return value* becomes the actual decorator.

## Type hints recap (surface-level)

You've been seeing these everywhere:

```python
x: int                       # x is an int
xs: list[str]                # list of strings
maybe: int | None            # union — int or None
fn: Callable[[int], str]     # function from int to str
fn2: Callable[..., int]      # function from any args to int
fn3: Callable[P, R]          # signature-preserving (decorators)
```

Phase 2's Module 8 covers Generic, TypedDict, Protocol, and friends.
For now: **hint your function signatures**. The cost is one line per
function; the payoff is editor help, type-check warnings, and easier
review.

## A small gotcha

```python
@retry         # forgot the parens — this passes `fn` as `times`
def fetch(): ...
```

`@retry` (no parens) tries to call `retry(fetch)` — which then runs
`if times < 1` against the function object. You'll get a confusing
error. Always include `()` for an arg-taking decorator, even if you
take all defaults.

## Now: open `02_fluency.py`

A 3-layer decorator is partially built. Patch the missing pieces.
