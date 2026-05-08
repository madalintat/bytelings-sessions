---
day: day-064-fixtures-and-parametrize
phase: phase-3-quality-production
module: module-12-testing-with-pytest
style: build-it
---
# Day 64 — Build a fixture (because pretend pytest doesn't have them)

Imagine pytest didn't ship `tmp_path`. You're writing tests that need
a fresh temp directory each time. You'd write this:

```python
def test_one():
    d = tempfile.mkdtemp()
    try:
        # ... use d ...
    finally:
        shutil.rmtree(d)

def test_two():
    d = tempfile.mkdtemp()
    try:
        # ... use d ...
    finally:
        shutil.rmtree(d)
```

The setup/teardown ritual sits inside every test. Move five tests in,
the noise drowns the intent. **A fixture is just that ritual extracted
into a function pytest will inject for you.**

## Building a fixture from scratch

```python
import pytest, tempfile, shutil
from pathlib import Path

@pytest.fixture
def workdir():
    d = Path(tempfile.mkdtemp())
    yield d                # <-- the test runs HERE, with d as the value
    shutil.rmtree(d)        # cleanup, after the test
```

That's the whole shape. The `yield` is the seam: everything before is
setup, the yielded value is what the test receives, everything after
is teardown. Add `workdir` as a parameter to any test:

```python
def test_writes_a_file(workdir):
    (workdir / "out.txt").write_text("hello")
    assert (workdir / "out.txt").read_text() == "hello"
```

pytest matches the parameter name to a fixture and injects the result.
You never call `workdir()` yourself.

## Built-in fixtures you'll reach for

| Fixture | What it gives you |
|---|---|
| `tmp_path` | A fresh `pathlib.Path` directory, auto-cleaned. |
| `capsys` | `.readouterr()` returns captured stdout/stderr. |
| `monkeypatch` | Set/undo env vars, attrs, dict items, just for this test. (Day 65.) |
| `request` | Metadata about the running test. Power-user only. |

## Scope: when does the fixture run?

Default scope is `function` — run before each test, tear down after.
Other scopes:

- `module` — once per test file. Good for things expensive but read-only.
- `session` — once per `pytest` invocation. Use sparingly; shared state
  is a test-flake factory.

```python
@pytest.fixture(scope="module")
def db_connection():
    conn = connect()
    yield conn
    conn.close()
```

## Parametrize: same test, many inputs

You wrote five tests yesterday with the same shape, different inputs.
That's a `@pytest.mark.parametrize` away from one test:

```python
@pytest.mark.parametrize("text, expected", [
    ("",        0),
    ("hello",   2),
    ("rhythm",  0),
    ("HELLO",   2),
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
```

Failure messages call out *which* parameter set failed. You get four
test cases for one function body, and the diff stays loud and clear.

You can stack parametrize decorators (Cartesian product), and you can
parametrize fixtures themselves (the same fixture body, run once per
parameter). But the basic form above is what you'll use 95% of the time.

## Now: open `fluency.py`

A test file with five duplicated tests. Collapse them into one
parametrized test. The tested function is fine.
