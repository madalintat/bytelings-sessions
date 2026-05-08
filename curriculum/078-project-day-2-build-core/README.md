---
day: day-078-project-day-2-build-core
phase: phase-3-quality-production
module: phase-3-project-log-analyzer
style: story
---
# Day 78 — Project Day 2: Build the core

Yesterday you nailed the line-level parser. Today the tool grows up:
walk a directory, parse every line, aggregate counts, and emit a real
summary. Logging instead of `print`, EAFP for malformed lines,
domain-specific exceptions in their right places.

## Today's slice

You'll implement the `Analyzer` — the heart of the tool. It owns:

1. **`Aggregate`** — a dataclass that holds running counts as the
   analyzer scans. `parsed`, `skipped`, `levels: Counter`,
   `top_paths: Counter`. Mergeable: `Aggregate.merge(other)`.
2. **`analyze_text(text) -> Aggregate`** — the per-text analyzer.
   Walks lines, tries to parse each, counts the result.
3. **`analyze_paths(paths) -> Aggregate`** — the multi-file driver.
   Reads each file, calls `analyze_text`, merges into a single
   aggregate. *Serial today*; tomorrow you'll parallelize.

## EAFP in the loop

You'll see this exact shape often in production:

```python
for line in text.splitlines():
    try:
        rec = parse_line(line)
    except MalformedLine:
        agg.skipped += 1
        log.debug("skipping malformed: %s", line[:80])
        continue
    agg.parsed += 1
    agg.levels[rec.level] += 1
    path = rec.fields.get("path", "<no-path>")
    agg.top_paths[path] += 1
```

Try the operation. Handle the specific exception. Move on. The
`log.debug` line is your audit trail at debug verbosity — silent in
prod, available with one CLI flag.

## Why merge() matters

Today the merge is just "two aggregates from two files." Tomorrow,
each child process produces an aggregate; the parent merges them.
That symmetry is by design — *commutative, associative aggregates
parallelize trivially*.

```python
@dataclass
class Aggregate:
    parsed: int = 0
    skipped: int = 0
    levels: Counter = field(default_factory=Counter)
    top_paths: Counter = field(default_factory=Counter)

    def merge(self, other: "Aggregate") -> "Aggregate":
        return Aggregate(
            parsed=self.parsed + other.parsed,
            skipped=self.skipped + other.skipped,
            levels=self.levels + other.levels,        # Counter + Counter
            top_paths=self.top_paths + other.top_paths,
        )
```

Counters add as multisets (the `+` operator). Two-line merge.

## The logging seam

A library should never call `logging.basicConfig`. That's the
*application's* job (the CLI in rung 5). Inside library code:

```python
import logging
log = logging.getLogger(__name__)
```

Then `log.debug(...)`, `log.info(...)`, etc. The CLI wires up the
handlers and formatters. This split is what makes the analyzer
embeddable in a bigger app later without log-config conflicts.

## Now: open `02_fluency.py`

A near-complete `Aggregate` with one missing piece: the `merge`
method. Add it.
