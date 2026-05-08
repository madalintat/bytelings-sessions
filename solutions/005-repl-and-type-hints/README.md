---
day: 005-repl-and-type-hints
phase: phase-1-python-core
module: module-01-setup-and-values
style: tour
---
# Day 5 — Read this typed function

Here's a small function from a real codebase. Read it line by line.

```python
from pathlib import Path


def total_size(directory: Path, suffix: str = ".txt") -> int:
    """Sum the sizes (in bytes) of files in `directory` matching `suffix`."""
    return sum(
        f.stat().st_size
        for f in directory.iterdir()
        if f.is_file() and f.suffix == suffix
    )
```

Walk through it:

1. **`from pathlib import Path`** — Path is a class for filesystem paths.
   You'll meet it deeply in Module 10, but here it's just an annotation.
2. **`def total_size(directory: Path, suffix: str = ".txt") -> int:`** —
   This is a *type-annotated signature*:
   - `directory: Path` — the parameter is expected to be a `Path` object.
   - `suffix: str = ".txt"` — a string with a default of `".txt"`.
   - `-> int` — the function returns an `int` (number of bytes).
3. **The body** — a generator expression summed to `int`. We'll cover
   generators in Module 6; for today, just notice it reads naturally.

## What type hints actually do

Type hints are **annotations** — they don't change runtime behavior.
Python won't crash if you pass a string where a `Path` was hinted.
But:

- Editors use them for autocomplete and error squiggles.
- `mypy` (or `pyright`) can statically check your code.
- They're documentation that doesn't go stale.

You write them mostly for the next reader. Often that next reader is
future-you, six months from now.

## The REPL is your friend

Anytime you're unsure, drop into the REPL:

```bash
uv run python
>>> from pathlib import Path
>>> p = Path(".")
>>> p.iterdir()
<generator object Path.iterdir at 0x...>
>>> list(p.iterdir())[:3]
[...]
```

Tab-completion works. `help(thing)` works. `dir(thing)` works.

For deeper inspection: `uv run python -i your_file.py` runs the file
*then* drops into REPL with all your names available.

## Now: `fluency.py`

Add the missing type hints. The tests check the *annotations* exist,
not just the runtime behavior.
