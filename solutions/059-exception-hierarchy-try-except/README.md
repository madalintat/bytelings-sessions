---
day: day-059-exception-hierarchy-try-except
phase: phase-3-quality-production
module: module-11-errors-eafp-debugging
style: tour
---
# Day 59 — A guided tour of Python's exception hierarchy

You're paged at 2 AM. Your service is crashing on bad input and the
traceback shows:

```text
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'N/A'
```

Before you can fix it, you need a map of *what kind of thing*
`ValueError` is. Python's exceptions form a tree. The closer you catch
to the leaf, the safer your handler is.

## The tour

```text
BaseException
 ├── SystemExit         # sys.exit() — don't catch
 ├── KeyboardInterrupt  # Ctrl-C — don't catch in services
 └── Exception          # everything you'd ever want to catch
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError    # list[99]
      │    └── KeyError      # dict["missing"]
      ├── OSError            # files, sockets, permissions
      │    ├── FileNotFoundError
      │    └── PermissionError
      ├── ValueError         # right type, wrong value
      ├── TypeError          # wrong type entirely
      └── ...
```

Two rules drop out of this tree:

1. **Never catch `BaseException`** (or bare `except:`). You'll swallow
   `Ctrl-C` and `SystemExit` and end up with a process that won't die.
2. **Catch the narrowest thing that makes sense.** `except Exception`
   in production code is a code smell — you're saying "I have no idea
   what could go wrong here." A reviewer will (rightly) push back.

## try / except / else / finally — the full shape

Most Python code uses `try` and `except`. The other two clauses earn
their keep in production:

```python
try:
    raw = path.read_text()
except FileNotFoundError:
    log.warning("config missing, using defaults")
    raw = DEFAULT_CONFIG
else:
    log.info("config loaded from %s", path)
finally:
    metrics.increment("config.read_attempted")
```

- `else` runs only if `try` succeeded. Put code here that should run
  *but you don't want its exceptions caught by the `except`* above.
- `finally` runs no matter what — success, handled exception, or
  uncaught exception on the way out. Use it for cleanup (closing a
  socket, releasing a lock).

## Catching multiple types

```python
except (FileNotFoundError, PermissionError) as e:
    log.error("could not read %s: %s", path, e)
```

A tuple of types catches any of them. Bind with `as e` only if you
actually use `e` — otherwise drop it. `e` goes out of scope when the
`except` block exits (a deliberate cleanup choice, not a quirk).

## Now: open `fluency.py`

Two `except` clauses are too broad. Tighten them.
