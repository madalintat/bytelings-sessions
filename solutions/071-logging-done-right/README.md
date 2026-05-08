---
day: day-071-logging-done-right
phase: phase-3-quality-production
module: module-14-logging-profiling-perf
style: pain
---
# Day 71 — When `print` was free and now you can't grep

Three months ago, you sprinkled `print` statements through a service
because they were easy. Today, the service is paged at 3 AM, the
operator can't tell which prints are real warnings vs debug noise,
and there's no timestamp so you can't even line up events. You wish
you'd used `logging` from day one.

## The pain of `print`

```python
print(f"got request for {user_id}")
print(f"db error: {e}")
print(f"sent email to {addr}")
```

Three problems by morning:

1. **Nothing is sortable.** No timestamp, no level, no source.
2. **You can't turn anything off.** "Set log level to WARNING" isn't
   a thing print supports. You'd be commenting out lines.
3. **You can't redirect.** Every print goes to stdout. In production
   you want errors to a file, debug to nowhere, info maybe to syslog.

The standard library's `logging` module solves all three with one
line of setup. People avoid it because the docs are intimidating.
Here's what you actually need.

## The five-line setup that works

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)
```

`logging.getLogger(__name__)` is the line you'll repeat in every
module. The logger's name becomes the module path — that gives you
`myapp.email` vs `myapp.db` in the output, and you can filter by
prefix.

## The five levels (and how to pick)

| Level | Use for |
|---|---|
| `DEBUG` | Internal detail. Off in production. "request_id=abc, retry=2." |
| `INFO` | Normal lifecycle events. "Service started." "Job 42 done." |
| `WARNING` | Something unexpected but recoverable. "Cache miss; fetching." |
| `ERROR` | A failure. The user's request failed; we're still up. |
| `CRITICAL` | Service-wide. "Out of disk." "Database unreachable." |

Rule of thumb: if a human would want a pager on it, `ERROR` or
`CRITICAL`. If they want to *know* but don't have to act, `WARNING`.

## The %s trap (and why you avoid f-strings here)

```python
# DON'T:
log.info(f"got {user_id} from {endpoint}")

# DO:
log.info("got %s from %s", user_id, endpoint)
```

Why? When the level is filtered out (e.g., DEBUG in prod), the
`%s` form skips the formatting work entirely. The f-string already
formatted *before* `log.info` was called. For hot paths, that matters.
For all paths, it's the convention readers expect.

Bonus: when you log structured records (e.g., to JSON), the args
stay separate from the message template — perfect for log aggregators
that parse `event=user_login user_id=42`.

## `log.exception` — the one method everybody misses

Inside an `except` block, use `log.exception` to capture the
traceback automatically:

```python
try:
    risky()
except Exception:
    log.exception("risky() blew up")  # includes the traceback in the log
```

Same level as `ERROR`, but the entire traceback is in the log line.
Future-you, paged at 3 AM, will be grateful.

## Now: open `02_fluency.py`

Convert prints to logger calls at the right levels.
