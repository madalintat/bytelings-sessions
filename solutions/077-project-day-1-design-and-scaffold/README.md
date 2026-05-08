---
day: day-077-project-day-1-design-and-scaffold
phase: phase-3-quality-production
module: phase-3-project-log-analyzer
style: story
---
# Day 77 — Project Day 1: Design and scaffold

You're building the **Parallel Log Analyzer**. The team ops manager
just ran a 4 GB log dump through `grep` and got nothing useful. They
want a real tool — one they can re-run during an incident, fast enough
that nobody complains.

You can't write the parallel speedup until you can parse a single line
correctly. That's today.

## Today's slice

1. **One dataclass.** A `LogRecord` with `ts`, `level`, `fields`
   (a dict of the body's `key=value` tokens).
2. **One parser.** `parse_line(text) -> LogRecord` — raises a custom
   `MalformedLine` exception when the input doesn't conform.
3. **One synthetic-fixture helper.** A `make_log_text(n)` that
   produces `n` lines of valid log output for tests. Real log files
   are gigabytes; we want a deterministic, in-memory fixture.

## The log format

```text
2026-05-08T10:00:00 INFO  path=/users status=200 took_ms=15
2026-05-08T10:00:01 ERROR path=/db    status=500 detail=conn_refused
```

- ISO-8601 timestamp at column 0.
- Whitespace.
- Level: one of DEBUG / INFO / WARN / ERROR (as written).
- Whitespace.
- Body: zero or more `key=value` tokens, whitespace separated.
  No quoting. (The `shlex` upgrade is in tomorrow's stretch.)

A line that doesn't match — empty, missing level, malformed timestamp
— is *not silently ignored*. Today's parser raises `MalformedLine`,
and tomorrow's aggregator catches that exception and records a count.
That separation of concerns is the whole point of a custom exception.

## Why a dataclass

You'll touch `LogRecord` everywhere. A dict is fine but unstructured;
typos like `record["levle"]` fail at runtime. A dataclass:

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class LogRecord:
    ts: datetime
    level: str
    fields: dict[str, str] = field(default_factory=dict)
```

Now `record.level` is type-checked, autocompletes in your editor, and
the printable repr is debuggable for free.

## Why one file today

Project rungs swap "five concept rungs" for "today's slice of the
project." The rungs:

- **Rung 2 (fluency):** finish the `LogRecord` dataclass.
- **Rung 3 (guided):** implement `parse_line`.
- **Rung 4 (solo):** implement `make_log_text` and a `MalformedLine`
  custom exception with a useful message.
- **Rung 5 (apply):** parse a multi-line input and count records by
  level. (You'll grow this into a real aggregator tomorrow.)

The story holds: same domain, same data shape, building tomorrow's
foundation today.

## Now: open `fluency.py`

A near-complete `LogRecord` with one TODO. Then keep walking up.
