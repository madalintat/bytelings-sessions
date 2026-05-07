# Phase 3 Project — Parallel Log Analyzer

## The Scenario

You're on the platform team at a B2B SaaS. Every service writes a
shared log format to a directory of rotated files. The on-call team
wants a tool: point it at the log directory, get a summary report —
top errors, request rate per minute, slow endpoints — fast enough
that they can re-run it during an incident without it being the
bottleneck.

You ship a CLI tool, in three days. Production-grade: real logging,
real tests, profiled, and parallel where it pays.

## Requirements

The tool must:

1. Parse a directory of plain-text log files matching a known format.
2. Produce a structured summary:
   - Total lines parsed and skipped.
   - Counts per log level (DEBUG, INFO, WARN, ERROR).
   - Top N error messages.
   - Lines per minute (a small histogram).
3. Use `logging` (NOT `print`) with sensible defaults: INFO to
   stderr, with timestamps and levels.
4. Have a pytest suite that exercises the parser, the aggregator, and
   the CLI end-to-end on a small synthetic fixture.
5. Run a profile pass (`cProfile`) and have at least one
   parallelization win — a measurable speedup over the serial path
   on a multi-file input.
6. Ship as a single `analyzer/` package, runnable as
   `python -m analyzer <log_dir>`.

## Concepts checklist (from this phase)

- M11: exception hierarchy, custom exceptions, EAFP, breakpoint, systematic debugging
- M12: pytest, fixtures, parametrize, monkeypatch, property-based testing
- M13: reading code, refactoring, pythonic style
- M14: logging done right, cProfile, "why is this slow"
- M15: GIL, threads vs async vs procs, multiprocessing patterns

## Day-by-day plan

### Day 1 — Design and scaffold
- Sketch the data model (one `LogRecord` dataclass).
- Build a parser that turns a single line into a record OR raises a
  custom `MalformedLine` exception.
- Build the synthetic fixture-generator (so tests don't depend on
  a real log directory).
- Tests pin behavior of the parser at the line level.

### Day 2 — Build the core
- Walk a directory, parse all lines, aggregate.
- Use a `defaultdict`/`Counter`-driven aggregator.
- Wire up logging (no prints anywhere).
- A first end-to-end test.

### Day 3 — Test, profile, and ship
- Profile a serial multi-file run.
- Add a parallel path (`ProcessPoolExecutor` over files).
- Confirm a measurable speedup vs serial.
- Polish the CLI and tests.

## Graduated hints

<details>
<summary>Hint: log line format</summary>

A reasonable format is:

```text
2026-05-08T10:00:00 INFO  request.id=42 path=/users status=200 took_ms=15
2026-05-08T10:00:01 ERROR request.id=43 path=/db    status=500 detail="connection refused"
```

A space-delimited prefix (`<iso_ts> <LEVEL> ...`) plus key=value
tokens for the body. Use `shlex.split` or a simple `str.split` if you
disallow quoted values.
</details>

<details>
<summary>Hint: parallelism strategy</summary>

The unit of parallel work is a *file*. Each file is independent — you
parse it, return a partial aggregate. The main process merges
partials. Use `ProcessPoolExecutor` and a top-level `parse_file(path)`
worker.
</details>

## Stretch goals

- A `--json` mode that emits machine-readable output.
- A `--since`/`--until` time filter.
- An async file-tail mode (watch a single file).
- A flame graph via `pyinstrument`.

## Self-evaluation rubric

- [ ] No `print` calls anywhere — only `logging`.
- [ ] At least one `pytest.mark.parametrize` test.
- [ ] At least one `monkeypatch` usage.
- [ ] A `MalformedLine` (or similar) custom exception.
- [ ] A profile dump committed (or a comment with the top 3 hotspots).
- [ ] A measurable speedup from the parallel path (CLI prints both
      timings or a comment captures them).
- [ ] CI-quiet: `uv run pytest` is green; no warnings.
