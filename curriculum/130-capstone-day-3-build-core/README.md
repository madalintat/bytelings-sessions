---
day: day-130-capstone-day-3-build-core
phase: phase-6-packaging-ast-capstone
module: capstone
style: build-it
---
# Capstone Day 3 — Build the core

You have a CLI shell. Today you make `habit done <name>` actually
record something to disk, and `habit list` actually read it back.

This is the meaty day. By tonight your tool *works* — just barely.

## The slice

Three things to build:

1. **Storage** — a `Database` class in `storage.py` that loads/saves
   a JSON file atomically. "Atomically" matters: if the user hits
   Ctrl-C mid-write, the old file should still be intact. Pattern:
   write to a temp file, then `os.replace` over the real one.
2. **Domain model** — a `Habit` dataclass in `core.py` with
   `name: str`, `created: date`, `log: list[date]`. Add a
   `mark_done(today)` method and a `streak(today)` method.
3. **Wire-up** — replace the TODO in `cli.py done`. Load the DB,
   call `mark_done`, save the DB, print a friendly confirmation.

## Concepts you're using

This is where the curriculum pays off. From across all six phases:

- **Dataclasses (M8)** — `@dataclass` for `Habit`. `field(default_factory=list)`
  for the log. `__post_init__` if you parse `date` from strings.
- **Files + JSON (M10)** — `json.dump`, `Path.write_text`,
  `tempfile.NamedTemporaryFile` for atomic writes.
- **Context managers (M9)** — `with` for the temp file lifecycle.
- **EAFP / errors (M11)** — handle "file doesn't exist yet" with
  `try/except FileNotFoundError`, not `if path.exists()`.
- **Type hints (M5/M8)** — annotate every function. `Path`, `date`,
  `dict[str, Habit]`.
- **Streak calc (M22-flavor)** — count consecutive days backward from
  `today` that appear in `log`. Exactly one loop.

## The atomic-write pattern, briefly

The naive way:

```python
path.write_text(json.dumps(data))
```

If this is interrupted, the file is half-written. The atomic way:

```python
import tempfile, os, json
from pathlib import Path

def save_atomic(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.NamedTemporaryFile(
        "w", dir=path.parent, delete=False, encoding="utf-8"
    )
    try:
        json.dump(data, tmp, indent=2)
        tmp.flush()
        os.fsync(tmp.fileno())
        tmp.close()
        os.replace(tmp.name, path)
    except Exception:
        os.unlink(tmp.name)
        raise
```

`os.replace` is atomic on POSIX *and* Windows. This pattern shows up
in every database, every config tool, every "save to disk" library.
It's worth knowing once and reusing forever.

## Today's deliverable

When you're done:

- [ ] `habit done meditate` writes `~/.config/habit/data.json`
      (or whatever path you configured)
- [ ] `habit done meditate` *again* on the same day is idempotent
      (no duplicate log entries)
- [ ] `habit list` reads the file and prints habits with streak counts
- [ ] `tests/test_core.py` passes

A starter `Database` and `Habit` are in this folder with the hard
parts left as TODOs. You can also rewrite from scratch — your call.

## A choice you have to make today

What does `habit done meditate` do if the habit doesn't exist yet?
Two reasonable answers:

(a) **Auto-create.** Quietly add it the first time you mark it done.
    Lower friction. What I'd pick.
(b) **Require explicit `habit add`.** More structured. More commands.

Pick one. Document it (in `design.md` from yesterday). Move on.

## Next

Tomorrow: features. `list`, `reset`, maybe `recent` or a multi-habit
filter. The scaffolding is done. From here it's just code.
