---
day: 023-defining-and-calling-functions
phase: phase-1-python-core
module: module-05-functions-closures-decorators
style: tour
---
# Day 23 — A guided tour of one well-shaped function

Read this. Notice every choice.

```python
def normalize_phone(raw: str, *, country: str = "US") -> str:
    """Strip a phone number to digits, optionally with a country prefix.

    Args:
        raw: a phone number with any formatting.
        country: 'US' (default) prepends '1' if missing.

    Returns:
        A digits-only string with the appropriate country prefix.
    """
    digits = "".join(c for c in raw if c.isdigit())
    if country == "US" and len(digits) == 10:
        digits = "1" + digits
    return digits
```

Twelve things this snippet says without saying them:

1. **`def name(...) -> RetType:`** — type hints on parameters and the
   return type. Optional but expected in modern Python.
2. **`raw: str`** — `raw` is positional. Callers pass it first, with
   or without naming it.
3. **`*, country: str = "US"`** — the bare `*` says "every parameter
   to my right is **keyword-only**." So callers must write
   `normalize_phone("...", country="UK")`, not `normalize_phone("...", "UK")`.
   This is one of the highest-leverage syntax features in Python: it
   turns "what does this second positional argument mean?" into a
   compile-time error.
4. **`= "US"`** — default value. Evaluated **once**, at definition
   time. (Default-arg trap is Day 24.)
5. **The triple-quoted docstring** — Google-style. First line is a
   one-sentence summary, then a blank line, then sections. `pydoc`
   and IDE help use this; tests reference it.
6. **`Args:` / `Returns:`** — convention; pick one (Google, Sphinx,
   NumPy) and stick with it. We use Google in this curriculum.
7. **Body short, single purpose** — one parse, one prefix, return.
   If a function does *and-then-and-then*, split it.
8. **`return`** — explicit. A function with no `return` returns `None`.
9. **No mutation of inputs.** `raw` is a string (immutable anyway),
   but the rule generalizes: make a new value and return it. Functions
   that *only* mutate are useful, but rare. The default is "pure."
10. **Naming.** Lowercase, snake_case. The function name is a verb.
11. **Helper hygiene.** `digits = ...` is a local variable; it dies
    when the function returns. The function leaves no trace.
12. **Calling looks like:** `normalize_phone("415-555-1212")`,
    `normalize_phone("020 7946 0958", country="UK")`. Read at the
    callsite, not at the definition.

## A second example, tinier still

```python
def clamp(x: float, lo: float, hi: float) -> float:
    """Constrain x to the [lo, hi] range."""
    return max(lo, min(x, hi))
```

Three positional params, one return. The `max(lo, min(x, hi))` idiom
is worth memorizing — it does the clamp without an `if`.

## A few rules of thumb

- **Hint everything you can.** Even when not enforced, types help the
  reader and lint tools.
- **Prefer keyword-only for flags.** Anything `bool` should be passed
  by name, not by position. `do_thing(x, force=True)` reads; `do_thing(x, True)` doesn't.
- **A function that doesn't return *anything useful* should return
  `None` explicitly** (or just have no `return`).
- **Docstring tells you what** *the function* **does**, not *how*. The
  body shows how.

## Now: open `fluency.py`

Three small function shapes are slightly off. Match the spec.
