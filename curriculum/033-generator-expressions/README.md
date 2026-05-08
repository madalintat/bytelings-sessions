---
day: day-033-generator-expressions
phase: phase-2-pythonic-tools
module: module-06-comprehensions-iterators-generators
style: compare
---
# Day 33 — `[ ]` vs `( )`: list comp vs generator expression

Two snippets. Same shape. One memory disaster, one not.

```python
# A — list comprehension
total = sum([n * n for n in range(10_000_000)])
```

```python
# B — generator expression
total = sum(n * n for n in range(10_000_000))
```

The only visible difference is the brackets. The runtime difference is
huge. Snippet A builds an 80 MB list of 10 million squares, *then* sums
it. Snippet B never builds the list — it produces one square, hands it
to `sum`, the running total updates, the next square is produced. Peak
memory: a few bytes.

## What a generator expression is

A generator expression has the same grammar as a comprehension but with
parens. Instead of returning a container, it returns a **generator
object** — an iterator that produces values on demand.

```python
gen = (n * n for n in range(5))
next(gen)  # 0
next(gen)  # 1
next(gen)  # 4
```

You can `for ... in` it, pass it to `sum`, `max`, `any`, `all`, `min`,
`set`, `dict`, `list`, `"".join(...)` — anything that takes an iterable.

## When to pick which

| Use a list comp `[...]` when | Use a generator expr `(...)` when |
|---|---|
| You need the result twice | You consume it once |
| You need indexing or `len()` | You only iterate forward |
| The collection is small | The collection is large or unknown |
| You need to mutate it later | You're piping it into `sum`/`max`/`any` |

A subtle bonus: when a generator expression is the *only* argument to a
function, you can drop one pair of parens:

```python
sum(n * n for n in nums)        # clean
sum((n * n for n in nums))      # works, but redundant
any(x < 0 for x in values)      # clean
```

## The footgun

Generators are **single-use**. After you iterate once, they're empty.

```python
gen = (n for n in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # []  ← already consumed
```

If you find yourself wanting to iterate twice, that's the signal to
make it a list. Otherwise, prefer the generator — the default answer
when streaming data is "lazy."

## Now: open `fluency.py`

You'll convert two memory-hungry list comps into generator expressions.
