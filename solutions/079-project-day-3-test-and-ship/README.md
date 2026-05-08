---
day: day-079-project-day-3-test-and-ship
phase: phase-3-quality-production
module: phase-3-project-log-analyzer
style: story
---
# Day 79 — Project Day 3: Test, profile, ship

The analyzer works. Today is the difference between "works on my
machine" and "ships." Three steps:

1. **Profile** the serial path on a synthetic multi-file input.
   Record the top hotspots. (Day 72.)
2. **Parallelize** at the file level using `ProcessPoolExecutor`.
   Confirm a measurable speedup. (Days 74 & 76.)
3. **End-to-end test** the parallel path produces *the same*
   aggregate as the serial path on the same input. (Day 12.)

## Why parallelism is the natural fit

`analyze_text` per file is **CPU-bound** (string parsing in Python).
It's also **independent** — each file's aggregate doesn't depend on
the others. And `Aggregate.merge` is associative and commutative.
That checklist (CPU-bound, independent, mergeable) is the textbook
case for `ProcessPoolExecutor` over files: each worker reads one
file, parses it, returns an `Aggregate`; the parent merges.

```python
from concurrent.futures import ProcessPoolExecutor
from functools import reduce

def analyze_paths_parallel(paths, max_workers=None):
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        partials = list(pool.map(_analyze_one_path, paths))
    return reduce(Aggregate.merge, partials, Aggregate())
```

`_analyze_one_path` must be a top-level function (the pickle wall,
Day 76). The aggregate must be picklable — a dataclass of ints +
Counters is, by default.

## The two timings to capture

In your CLI today you'll print:

```text
serial:    1820 ms
parallel:   430 ms  (4.2x)
```

That's a real speedup, not a vibe. The number depends on `cpu_count`,
file size, and parser complexity, but as long as it's > 2x on a
multi-core box, the parallel path earned its complexity.

## End-to-end equivalence: the test that matters

```python
def test_parallel_matches_serial(tmp_path):
    paths = make_synthetic_files(tmp_path, n_files=4, n_lines=500)
    a = analyze_paths(paths)
    b = analyze_paths_parallel(paths)
    assert a.parsed == b.parsed
    assert a.skipped == b.skipped
    assert a.levels == b.levels
    assert a.top_paths == b.top_paths
```

This test catches every "I introduced a subtle bug while parallelizing"
mistake at once. **Run it, then ship.**

## What you ship

A real project would have an `analyzer/` package. For curriculum
flow, the rungs today are:

- **Rung 2 (fluency):** profile + read the hotspots.
- **Rung 3 (guided):** implement `analyze_paths_parallel`.
- **Rung 4 (solo):** the end-to-end equivalence test, plus any
  helpers the test needs.
- **Rung 5 (apply):** the CLI prints both timings + the speedup.

When you finish today, you have a tool you can take to a real log
directory and run.

## Now: open `fluency.py`

Profile a small analyzer run and identify the hotspot.
