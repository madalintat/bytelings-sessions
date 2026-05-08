---
day: 026-first-class-functions-and-lambdas
phase: phase-1-python-core
module: module-05-functions-closures-decorators
style: metaphor
---
# Day 26 — Functions are pets, not appliances

Most languages treat a function like an appliance: you turn it on,
it does its job, you turn it off. Python treats a function like a
**pet** — a small living thing you can name, hand to a friend, leash
to another pet, or stuff in a bag.

In code terms: **functions are first-class values**. They have all
the same rights as integers and strings:

- You can **assign** them to a variable.
- **Pass** them as an argument.
- **Return** them from another function (Day 25 already did this).
- **Store** them in a list, dict, or set.

```python
def square(x): return x * x
def cube(x):   return x * x * x

ops = [square, cube]              # a list of functions
for f in ops:
    print(f(3))                   # 9, then 27

named = {"sq": square, "cu": cube}
named["sq"](4)                    # 16
```

That's it. Once you see it, callbacks, decorators, sorting, and
filtering all stop being magic.

## The `lambda`: a tiny throwaway pet

A `lambda` is a function with no name and one expression body. You
use it where giving the function a name would be theatrical:

```python
sorted(words, key=lambda w: len(w))           # by length
sorted(rows, key=lambda r: (r["age"], r["name"]))   # by tuple
```

Reading `key=lambda w: len(w)` as English: "for sorting purposes,
score each w by len(w)." For exactly this case, you'd actually write
`key=len` — `len` is a function too. But for "score by w's age, then
name" you need a tiny custom expression.

**Rule of thumb:** if the lambda body is more than ~20 chars or wants
a name, define a `def` instead. Lambdas excel at *naming what the
caller wants*, not at *naming the function itself*.

## Higher-order: functions that take functions

A function that takes a function as an argument is called
**higher-order**. Python's built-ins use this pattern everywhere:

| Builtin | Pattern |
|---|---|
| `sorted(iter, key=fn)` | sort by fn-derived score |
| `max(iter, key=fn)` / `min` | extremum by score |
| `map(fn, iter)` | apply fn to each |
| `filter(fn, iter)` | keep items where fn(x) is truthy |
| `functools.reduce(fn, iter)` | fold |

You'll write higher-order helpers of your own, especially in this
module:

```python
def retry(fn, *, times: int = 3):
    for _ in range(times):
        try:    return fn()
        except: continue
    raise RuntimeError("all retries failed")
```

`retry` doesn't know what `fn` does. It only cares that fn is callable.
This separation — caller knows the *what*, helper knows the *how* —
is the heart of Python's flexibility.

## A small gotcha worth seeing

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)
[f() for f in funcs]              # [2, 2, 2]   — late binding!
```

Day 25 covered this. The fix is `lambda i=i: i` — bind the value as a
default argument so each lambda captures its own.

## Now: open `fluency.py`

Three small higher-order helpers and one lambda. Patch them.
