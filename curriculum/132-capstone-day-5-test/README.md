---
day: day-132-capstone-day-5-test
phase: phase-6-packaging-ast-capstone
module: capstone
style: story
---
# Capstone Day 5 — Test it like a stranger built it

You wrote `habit`. You're proud of it. You also know exactly what
inputs you tried, which means you know exactly which inputs you
*didn't* try.

Today you pretend a stranger wrote this code and your job is to break
it. Then you write tests for the breaks. Then you fix the breaks. By
tonight, the test suite should be the thing you trust to know whether
the tool works — not your fingers in a terminal.

## Concepts you'll lean on

From phase 3 (quality + testing) and phase 1 (file IO):

- **`pytest` fixtures** (M12) — `tmp_path` is built in, gives you a
  fresh `Path` per test. Use it everywhere you read/write files.
- **`monkeypatch.setenv`** (M12) — set `HABIT_DATA` so your tests
  don't touch the user's real data file.
- **`CliRunner`** (click) — invoke the CLI in-process, capture
  output, capture exit code. No subprocess overhead.
- **Parametrize** (`@pytest.mark.parametrize`) (M12) — table-driven
  tests for the streak edge cases.
- **`pytest.raises`** — for the "what should this refuse to do" cases.

## The edge cases worth testing

After 4 days of building, here's the inventory:

**Streak math**
- log is empty → streak 0
- log has only future dates → streak 0
- log has today only → streak 1
- log has 100 consecutive days → streak 100
- log has 50 days then a gap then today → streak 1 (gap breaks it)
- duplicate dates in log (shouldn't happen, but if they do?) → ?

**Storage**
- file doesn't exist → load returns `{}`
- file is corrupt JSON → ? Decision: raise a clear error
- file has unknown keys → ignore them (forward compat)
- save then load → equal to original
- save twice (atomic write) → final file is the second save
- save with disk full → raises (untested in CI; verify by reasoning)

**CLI**
- `habit done meditate` then `habit done meditate` same day → idempotent
- `habit reset nonexistent` → exit code 1, error to stderr
- `habit reset existing --yes` → wipes without prompt
- `habit list` with no habits → friendly "no habits yet" message
- `habit done ""` (empty name) → reject, exit code 2

You won't write a test for every one of those. Pick the 8-12 that
matter most to you and write them. Use parametrize where it saves
typing.

## A test you'll be glad you wrote

```python
def test_atomic_write_survives_crash(tmp_path, monkeypatch):
    """If save() raises mid-write, the old file is intact."""
    path = tmp_path / "data.json"
    storage.save(path, {"a": Habit("a", date(2026, 5, 1))})
    original = path.read_text()

    # Patch json.dump to raise mid-write.
    def boom(*args, **kwargs):
        raise RuntimeError("disk full simulation")
    monkeypatch.setattr("json.dump", boom)

    with pytest.raises(RuntimeError):
        storage.save(path, {"b": Habit("b", date(2026, 5, 2))})

    # Old file untouched.
    assert path.read_text() == original
```

This is the test that catches the bug where someone "improves" the
storage code and accidentally breaks the temp-file pattern. The next
person to do that has a red light to stop them.

## Today's deliverable

- [ ] At least 12 tests across `test_core.py`, `test_storage.py`,
      `test_cli.py`
- [ ] All tests pass with `uv run pytest`
- [ ] At least one parametrized test
- [ ] At least one fixture-using test (`tmp_path`)
- [ ] At least one CliRunner test that checks output text *and* exit code

The starter has a `conftest.py` with a fixture that sets `HABIT_DATA`
to a tmp path so the suite never touches your real data file. Use it.

## Next

Tomorrow: refactor. With tests in place, you can clean up freely.
