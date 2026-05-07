---
day: day-053-pathlib-and-file-io
phase: phase-2-pythonic-tools
module: module-10-files-paths-json-csv-toml
style: story
---
# Day 53 — The morning the strings betrayed you

You're three weeks into a project. You wrote your file handling like
this:

```python
import os

base = "/var/data/exports"
filename = "report-2026-05-08.csv"
full = base + "/" + filename            # ".../exports/report-..."
if os.path.exists(full):
    with open(full) as f:
        content = f.read()
```

It worked on your laptop. It worked in CI. Then a Windows colleague
ran it and got `\\` mixed with `/` and one missing slash crashed the
deploy. You spent an afternoon hunting it down.

That's when you stopped doing path arithmetic with strings.

## `pathlib.Path`: paths as objects

```python
from pathlib import Path

base = Path("/var/data/exports")
full = base / "report-2026-05-08.csv"
if full.exists():
    content = full.read_text()
```

The `/` operator joins paths correctly on every OS. `Path.exists()`,
`Path.is_file()`, `Path.is_dir()` answer questions without `os.path`
ceremony. `read_text()` and `write_text()` are one-liners that handle
the open/close themselves.

## What `Path` gives you for free

```python
p = Path("/var/data/exports/report-2026-05-08.csv")
p.name          # 'report-2026-05-08.csv'
p.stem          # 'report-2026-05-08'
p.suffix        # '.csv'
p.parent        # Path('/var/data/exports')
p.parts         # ('/', 'var', 'data', 'exports', 'report-...')
```

Every one of these used to be a regex or a string-split. Now it's an
attribute. The cognitive load drops.

## Read and write, the easy way

```python
p = Path("config.json")

p.write_text('{"k": 1}')           # writes a string
data = p.read_text()                # reads it back

p.write_bytes(b"\\x00\\x01\\x02")     # binary write
raw  = p.read_bytes()                # binary read
```

For big files or line-by-line work, you still want `with p.open() as f`
(returns the same file object as built-in `open`). But for most config
files and small artifacts, `read_text` / `write_text` is correct.

## Listing and globbing

```python
folder = Path("logs")

for f in folder.iterdir():          # one level deep
    print(f.name)

for f in folder.glob("*.log"):      # one level, by pattern
    print(f.name)

for f in folder.rglob("*.log"):     # recursive, by pattern
    print(f)
```

`iterdir`, `glob`, `rglob` all return generators of `Path` objects.

## Creating directories

```python
out = Path("build/reports")
out.mkdir(parents=True, exist_ok=True)
```

`parents=True` makes intermediate dirs (`build/` if missing).
`exist_ok=True` doesn't error if the dir already exists. This pair is
the right default — saves you from try/except boilerplate.

## The leftover string operations

When you need a string for a library that doesn't speak `Path`, just
`str(p)` it. When something hands you a string, wrap it in `Path(s)`.
The boundary between the two is one function call.

## Now: open `02_fluency.py`

A function uses string concatenation for a path. Switch it to `Path`.
