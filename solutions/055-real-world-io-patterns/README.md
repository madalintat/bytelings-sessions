---
day: day-055-real-world-io-patterns
phase: phase-2-pythonic-tools
module: module-10-files-paths-json-csv-toml
style: pain
---
# Day 55 — Three I/O bugs that ship to production

You wrote a script that processes 50,000 records and writes a report.
It works on a sample of 100. You run it on the full set. Then:

1. You see partial output, then a crash, then a half-written file you
   can't tell apart from a real one.
2. You see your laptop swap to disk because you read 10 GB into a list.
3. You see "permission denied" on Windows because the file you wrote
   is still open somewhere.

Each one is a pattern. Each one has a fix that's now standard.

## Pain 1: a half-written file that looks valid

You wrote your output like this:

```python
out = Path("report.json")
out.write_text(json.dumps(records, indent=2))
```

If `json.dumps` is fine and the disk write completes, great. If the
process is killed mid-write, you get a half-formed file that may even
parse partially. Worse: a downstream job picks up the file and acts on
the partial data.

**The fix: write-then-rename (atomic file write).**

```python
import os, tempfile
from pathlib import Path

def atomic_write_text(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    os.replace(tmp, path)   # atomic on POSIX and Windows
```

`os.replace` is atomic at the filesystem level — readers either see
the old file or the new one, never a half-write. If the process
crashes, the `.tmp` file remains; the original is untouched.

## Pain 2: blowing memory on a big file

```python
text = Path("huge.csv").read_text()        # loads 10 GB
for line in text.splitlines():
    process(line)
```

You don't need `text` whole. You only need one line at a time.

**The fix: stream line-by-line.**

```python
with open("huge.csv") as f:
    for line in f:                          # iterates lazily
        process(line.rstrip("\n"))
```

A file object is itself an iterable — each `next` reads one line. The
memory profile stays flat regardless of file size.

For non-text streams, read in chunks:

```python
with open("huge.bin", "rb") as f:
    while chunk := f.read(64 * 1024):
        process(chunk)
```

## Pain 3: encoding "just works" until it doesn't

```python
Path("data.txt").read_text()               # uses platform default!
```

On Linux, that's UTF-8. On Windows, it might be cp1252. Your script
that worked on your laptop sees garbled text on a colleague's machine.

**The fix: be explicit.**

```python
Path("data.txt").read_text(encoding="utf-8")
Path("data.txt").write_text(out, encoding="utf-8")
open("data.txt", encoding="utf-8")
```

Always pass `encoding` for text I/O. UTF-8 is the right default 99%
of the time. The 1% where it isn't, you'll know.

## The principles, distilled

- **For correctness:** atomic writes for any file readers will pick up.
- **For scale:** stream line-by-line; never load whole files unless
  you must.
- **For portability:** always specify `encoding="utf-8"`.

Three small habits. They make the difference between code that's
fine on your laptop and code that doesn't blow up in production.

## Now: open `fluency.py`

A `save_report` function that's missing both atomicity and an encoding.
