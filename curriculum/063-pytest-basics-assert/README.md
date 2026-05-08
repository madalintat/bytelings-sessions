---
day: day-063-pytest-basics-assert
phase: phase-3-quality-production
module: module-12-testing-with-pytest
style: tour
---
# Day 63 — A guided tour of pytest

You've been *running* pytest for sixty-two days. Today you take the
tour: what's actually happening when `uv run pytest` finds your tests,
and the four building blocks that cover 90% of real-world testing.

## What pytest collects

Run `uv run pytest` in a folder and pytest walks the tree looking for:

- Files matching `test_*.py` or `*_test.py`.
- Inside those, **functions** named `test_*` and **methods** named
  `test_*` on classes named `Test*` (no `__init__`).

That's the whole discovery rule. You don't register anything. There's
no `main()`. The runner finds your tests by name and runs them.

## The plain `assert` is the API

Other test frameworks have `self.assertEqual(a, b)` and friends.
pytest's design choice is to take the language's `assert` keyword and
make its failure messages useful via AST rewriting.

```python
def test_split():
    parts = "a,b,c".split(",")
    assert parts == ["a", "b"]   # fails — pytest shows you both sides
```

The diff in the failure output is the magic — pytest rewrites your
assertion AST so a failure shows:

```text
E       assert ['a', 'b', 'c'] == ['a', 'b']
E         Right contains one less item: 'c'
```

You almost never need anything beyond `assert`. The four exceptions:

## Four building blocks you'll use weekly

### 1. `pytest.raises` — assert an exception was raised

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

To inspect the message, use the `as` form: `with pytest.raises(ValueError) as info: ...; assert "expected" in str(info.value)`.

### 2. `pytest.approx` — float comparison without flake

`0.1 + 0.2 == 0.3` is False (Day 2). In tests:

```python
assert 0.1 + 0.2 == pytest.approx(0.3)
```

### 3. `pytest.mark.parametrize` — one test, many cases

```python
@pytest.mark.parametrize("n, expected", [(0, True), (1, False), (-4, True)])
def test_is_even(n, expected):
    assert is_even(n) == expected
```

You'll see this constantly tomorrow. Today: just know it exists.

### 4. `tmp_path` and `capsys` — built-in fixtures

`tmp_path` is a temporary `pathlib.Path` that pytest cleans up after
the test. `capsys` captures stdout/stderr so you can assert what your
function printed. You add them as parameters; pytest injects them.

```python
def test_writes_a_log(tmp_path):
    log = tmp_path / "out.log"
    log.write_text("ok\n")
    assert log.read_text() == "ok\n"
```

That's the tour. Tomorrow: fixtures and parametrize in depth.

## Now: open `fluency.py`

A function and a half-broken test file. Make the tests pass.
